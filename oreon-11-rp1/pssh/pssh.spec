%global source0_hash dfe1b898e483377213b44b8316a81fd6e1bbe427e1607e76be18366071c04c85
Summary:        Parallel SSH tools
Name:          pssh
Version:       2.3.6
Release:        1%{?dist}
License:       LicenseRef-Callaway-BSD
Url:           https://github.com/lilydjwg/pssh
Source0:        https://github.com/lilydjwg/pssh/archive/refs/tags/v%{version}.tar.gz
Requires:      openssh-clients
BuildArch:     noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-pssh = %{version}-%{release}
# /oreon:deps
%description
This package provides various parallel tools based on ssh and scp.
Parallell version includes:
 o ssh : pssh
 o scp : pscp
 o nuke : pnuke
 o rsync : prsync
 o slurp : pslurp

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup
sed -i -e '1 d' psshlib/askpass_{client,server}.py

%build

%pyproject_wheel
%install
%pyproject_install
install -D -m 0755 %{buildroot}%{_bindir}/pssh-askpass \
    %{buildroot}%{_libexecdir}/pssh/pssh-askpass
rm -f %{buildroot}%{_bindir}/pssh-askpass
mv %{buildroot}%{_bindir}/pscp %{buildroot}%{_bindir}/pscp.pssh
install -d %{buildroot}%{_mandir}/man1
install -p -m 0644 man/man1/*.1  %{buildroot}%{_mandir}/man1
mv %{buildroot}%{_mandir}/man1/pscp.1 %{buildroot}%{_mandir}/man1/pscp.pssh.1
%oreon_autofiles main

%files

%changelog

%autochangelog
