%global source0_hash 8c50a2f10ab564d57746d7f1d61fa2faba717c5953ed2dc70c852a5311505994

Name:           python-flit-core
Version:        3.0.0
Release:        0%{?dist}
Summary:        Distribution-building parts of Flit

License:        BSD-3-Clause AND BSD-2-Clause
URL:            https://pypi.org/project/flit-core/
Source0:        https://github.com/takluyver/flit/archive/%{version}/flit-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros

%description
Test a wheel built from a subdirectory.
Test a build with pyproject.toml backend-path = .
flit-core builds with flit-core.


%package -n python3-flit-core
Summary:        %{summary}

%description -n python3-flit-core
...


%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -p1 -n flit-%{version}


%generate_buildrequires
cd flit_core
# this runtime-requires pytoml which is no longer available in Fedora
%pyproject_buildrequires -R
cd ..

%build
cd flit_core
%pyproject_wheel
cd ..


%install
%pyproject_install
# there is no license file marked as License-File, hence not using -l
%pyproject_save_files flit_core


%check
# internal check for our macros, we assume there is no license
grep -F %%license %{pyproject_files} && exit 1 || true


%files -n python3-flit-core -f %{pyproject_files}
