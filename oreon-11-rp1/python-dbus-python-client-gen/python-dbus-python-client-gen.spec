%global srcname dbus-python-client-gen

Name:           python-%{srcname}
Version:        0.8.4
Release:        %autorelease
Summary:        Python Library for Generating dbus-python Client Code

License:        MPL-2.0
URL:            https://github.com/stratis-storage/dbus-python-client-gen
Source0:        https://github.com/stratis-storage/dbus-python-client-gen/archive/v0.8.4/dbus-python-client-gen-0.8.4.tar.gz
# oreon url source checksums begin
%global source0_sha256 3561d2f55afce58f08fefb37b1ecd81b309c5e0ff0d720c5b2fa0882a9b30ac9
%global source0_file dbus-python-client-gen-0.8.4.tar.gz
# oreon url source checksums end

BuildArch:      noarch

%global _description \
%{summary}.

%description %{_description}

%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-devel

%description -n python3-%{srcname} %{_description}

Python 3 version.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/dbus-python-client-gen-0.8.4.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "3561d2f55afce58f08fefb37b1ecd81b309c5e0ff0d720c5b2fa0882a9b30ac9" || { echo "oreon: Source0 SHA256 mismatch for dbus-python-client-gen-0.8.4.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%autosetup -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l dbus_python_client_gen

%check
%pyproject_check_import

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.8.4-1
- Prepare for Oreon 11 (RP1)
