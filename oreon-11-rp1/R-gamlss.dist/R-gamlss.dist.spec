%global source0_hash d2db3a7658799c2ef212aa18cb75a3ecf4f73faf8c13dfdc3c14b21ae0129069

Name:           R-gamlss.dist
Version:        %R_rpm_version 6.1-1
Release:        %autorelease
Summary:        Distributions for Generalized Additive Models for Location Scale and Shape

License:        GPL-2.0-only OR GPL-3.0-only
URL:            %{cran_url}
Source:         %{cran_source}

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  R-devel

%description
A set of distributions which can be used for modelling the response variables
in Generalized Additive Models for Location Scale and Shape, Rigby and
Stasinopoulos (2005), <doi:10.1111/j.1467-9876.2005.00510.x>. The distributions
can be continuous, discrete or mixed distributions. Extra distributions can be
created, by transforming, any continuous distribution defined on the real line,
to a distribution defined on ranges 0 to infinity or 0 to 1, by using a "log"
or a "logit" transformation respectively.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -c
# Fix permissions.
pushd gamlss.dist
chmod -x NAMESPACE R/*.R man/*.Rd src/ST3.?
popd

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
