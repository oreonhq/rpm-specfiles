%global source0_hash df54a6f37ccd3b3f0df7f557ad8d7bdd412152b568beccd8d71cd73d4a9343e6

%global srcname into-dbus-python

Name:           python-%{srcname}
Version:        0.8.2
Release:        %autorelease
Summary:        Transformer to dbus-python types

License:        Apache-2.0
URL:            https://github.com/stratis-storage/into-dbus-python
Source0:        https://github.com/stratis-storage/into-dbus-python/archive/v0.8.2/into-dbus-python-0.8.2.tar.gz

BuildArch:      noarch

%global _description \
Facilities for converting an object that inhabits core Python types, e.g.,\
lists, ints, dicts, to an object that inhabits dbus-python types, e.g.,\
dbus.Array, dbus.UInt32, dbus.Dictionary based on a specified dbus signature.

%description %{_description}

%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-devel


%description -n python3-%{srcname} %{_description}

Python 3 version.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l into_dbus_python

%check
%pyproject_check_import

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.8.2-1
- Prepare for Oreon 11 (RP1)
