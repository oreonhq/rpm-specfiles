%global source0_hash 9ab32da7710e0c74307ac7559e4e9d002d21092d98c9f48e59daebbff485d935
Name:           stratis-cli
Version:        3.9.1
Release:        1%{?dist}
Summary:        Command-line tool for interacting with the Stratis daemon
License:        Apache-2.0
URL:            https://github.com/stratis-storage/stratis-cli
Source0:        https://github.com/stratis-storage/stratis-cli/archive/refs/tags/v3.9.1.tar.gz#/stratis-cli-3.9.1.tar.gz
Requires:       (stratisd >= 3.8.2 with stratisd < 4.0.0)
ExclusiveArch:  %{rust_arches} noarch
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-stratis-cli = %{version}-%{release}
# /oreon:deps
%description
stratis provides a command-line interface (CLI) for
interacting with the Stratis daemon, stratisd. stratis
interacts with stratisd via D-Bus.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%pyproject_wheel
a2x -f manpage docs/stratis.txt
%install
%pyproject_install
%{__install} -Dpm0644 -t %{buildroot}%{_mandir}/man8 docs/stratis.8
%oreon_autofiles main

%check

%pyproject_check_import
%files

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.8.3-1
- Prepare for Oreon 11 (RP1)
