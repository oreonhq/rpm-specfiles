%global source0_hash 3c3064c1ca3795730d63a5640944e1241b1f29752eaa7edcb803dba9fe5e85cc

%global desc %{expand:
REQUest REcordingRequre [rekure] - Is Library for storing output of various
function and methods to persistent storage and be able to replay the stored
output to functions.}

Name:           python-requre
Version:        0.9.1
Release:        6%{?dist}
Summary:        Python library that allows re/store output of various objects for testing

License:        MIT
URL:            https://github.com/packit/requre
Source0:        %{pypi_source requre}
BuildArch:      noarch

BuildRequires:  python3-devel

%description
%{desc}

%package -n     python3-requre
Summary:        %{summary}

%description -n python3-requre
%{desc}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n requre-%{version}

%generate_buildrequires
# The -w flag is required for EPEL 9's older hatchling
%pyproject_buildrequires %{?el9:-w}

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files requre

%files -n python3-requre -f %{pyproject_files}
# Epel9 does not tag the license file in pyproject_files as a license. Manually install it in this case
%if 0%{?el9}
%license LICENSE
%endif
%doc README.md
%{_bindir}/requre-patch

%changelog
%autochangelog
