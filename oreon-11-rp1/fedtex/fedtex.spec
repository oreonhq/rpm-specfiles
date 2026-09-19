%global source0_hash 9b45be3dbb7b2882a591d96f6733dd8196b1932f05ef273a18867b6dfec7d167

Name:           fedtex
Version:        0.2
Release:        %autorelease
Summary:        Simple TeX dependency installer for Fedora

License:        MIT
URL:            https://pagure.io/fedtex
Source0:        https://releases.pagure.org/%{name}/%{name}-%{version}.tar.gz

Requires:       coreutils
Requires:       sed
Requires:       grep

BuildArch:      noarch

%description
%{summary}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build
# nothing to build

%install
install -p -m 0755 -D fedtex.sh $RPM_BUILD_ROOT/%{_bindir}/fedtex
install -p -m 0644 -D man/man1/fedtex.1 $RPM_BUILD_ROOT/%{_mandir}/man1/fedtex.1

%files
%license License
%doc Readme.md
%{_mandir}/man1/fedtex.*
%{_bindir}/fedtex

%changelog
%autochangelog
