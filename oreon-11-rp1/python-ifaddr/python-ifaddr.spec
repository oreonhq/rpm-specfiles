%global srcname ifaddr
%global _description \
ifaddr is a small Python library that allows you to find all the IP addresses\
of the computer.

Name:           python-%{srcname}
Version:        0.2.0
Release:        5%{?dist}
Summary:        Python library that allows you to find all the IP addresses of the computer

License:        MIT
URL:            https://pypi.org/project/ifaddr/
Source:         %{pypi_source}
# oreon url source checksums begin
%global source0_sha256 cc0cbfcaabf765d44595825fb96a99bb12c79716b73b44330ea38ee2b0c4aed4
%global source0_file ifaddr-0.2.0.tar.gz
# oreon url source checksums end

BuildArch:      noarch

%description %{_description}

%package -n python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}
BuildRequires:  python3-devel

%generate_buildrequires
%pyproject_buildrequires

%description -n python3-%{srcname} %{_description}

Python 3 version.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/ifaddr-0.2.0.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "cc0cbfcaabf765d44595825fb96a99bb12c79716b73b44330ea38ee2b0c4aed4" || { echo "oreon: Source0 SHA256 mismatch for ifaddr-0.2.0.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%autosetup -n %{srcname}-%{version}

%build
%pyproject_wheel

%install
%pyproject_install

%files -n python3-%{srcname}
%license LICENSE.txt
%doc README.rst
%{python3_sitelib}/%{srcname}/
%{python3_sitelib}/%{srcname}-*.dist-info/

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.2.0-5
- Prepare for Oreon 11 (RP1)
