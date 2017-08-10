function[] = create_supereeg_interpmap(data_fname, outfile, tau)

x = load(data_fname);
locs = cellfun(@str2num, x.struct.R, 'UniformOutput', false);
R = cat(1, locs{:});
c = x.struct.Correlation;

good_inds = ~isnan(c);
c = c(good_inds);
R = R(good_inds, :);

[R, i] = unique(R, 'rows');
c = c(i);

std_fname = 'MNI152_T1_2mm_brain.nii';

[~, Rstd, origin, ~, mask] = TFA_load_nii(std_fname);
s = exp(-tau.*pdist2(R, Rstd));
y = (c * s) ./ sum(s, 1);


%y = interp3(R(:, 1), R(:, 2), R(:, 3), c, Rstd(:, 1), Rstd(:, 2), Rstd(:, 3), 'spline');

cmu_to_nii(y, Rstd, false, outfile, mask, origin);




function[m] = str2mat_helper(s)
m = str2num(s);
