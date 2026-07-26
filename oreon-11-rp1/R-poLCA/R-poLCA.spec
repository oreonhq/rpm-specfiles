%global source0_hash ed8c60a42bff0402c9ba2f9ce1422dd171e711c1a64498c4d96010ddb29f6b16

Name:           R-poLCA
Version:        %R_rpm_version 1.6.0.1
Release:        %autorelease
Summary:        Polytomous variable Latent Class Analysis

License:        GPL-2.0-or-later
URL:            %{cran_url}
Source:         %{cran_source}

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  R-devel

%description
Latent class analysis and latent class regression models for polytomous
outcome variables.  Also known as latent structure analysis.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -c

%generate_buildrequires
%R_buildrequires

%build

%install
%R_install
%R_save_files

%check
%R_check

%files -f %{R_files}

%changelog
%autochangelog
