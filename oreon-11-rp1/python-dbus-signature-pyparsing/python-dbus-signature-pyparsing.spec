%global srcname dbus-signature-pyparsing

Name:           python-%{srcname}
Version:        0.4.1
Release:        %autorelease
Summary:        Parser for a D-Bus Signature

License:        Apache-2.0
URL:            https://github.com/stratis-storage/dbus-signature-pyparsing
Source0:        https://github.com/stratis-storage/dbus-signature-pyparsing/archive/v0.4.1/dbus-signature-pyparsing-0.4.1.tar.gz
# oreon url source checksums begin
%global source0_sha256 dae2cfa1326e5fcdd13a102f259dcd02130d7e6cc667ade3aa82a61984cc3338
%global source0_file dbus-signature-pyparsing-0.4.1.tar.gz
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
%(f=%{_sourcedir}/dbus-signature-pyparsing-0.4.1.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "dae2cfa1326e5fcdd13a102f259dcd02130d7e6cc667ade3aa82a61984cc3338" || { echo "oreon: Source0 SHA256 mismatch for dbus-signature-pyparsing-0.4.1.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%autosetup -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l dbus_signature_pyparsing

%check
%pyproject_check_import

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.4.1-1
- Prepare for Oreon 11 (RP1)
