Name:           python-pretend
Version:        1.0.9
Release:        %autorelease
Summary:        A library for stubbing in Python

License:        BSD-3-Clause
URL:            https://github.com/alex/pretend
Source0:        https://github.com/alex/pretend/archive/v1.0.9/pretend-1.0.9.tar.gz
# oreon url source checksums begin
%global source0_sha256 890313320280455daeaa11100e8b765093fee7839ae946de38333601fe544a16
%global source0_file pretend-1.0.9.tar.gz
# oreon url source checksums end

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-pytest


%description
Pretend is a library to make stubbing with Python easier.


%package -n python3-pretend
Summary:        A library for stubbing in Python


%description -n python3-pretend
Pretend is a library to make stubbing with Python easier.


%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/pretend-1.0.9.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "890313320280455daeaa11100e8b765093fee7839ae946de38333601fe544a16" || { echo "oreon: Source0 SHA256 mismatch for pretend-1.0.9.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%autosetup -n pretend-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l pretend


%check
%pyproject_check_import
%pytest -v


%files -n python3-pretend -f %{pyproject_files}
%doc README.rst


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.0.9-1
- Prepare for Oreon 11 (RP1)
