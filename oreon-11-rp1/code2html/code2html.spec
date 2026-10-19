%global source0_hash 1f1257ebb8f679594f0cb5254093c7a3698c5d0db1833ce1f0c6fd51f979bd2a
Name:           code2html
Version:        0.9.1
Release:        51%{?dist}
Summary:        Convert source code to HTML
License:        MIT
URL:            http://www.palfrader.org/code/%{name}
Source0:        http://www.palfrader.org/code2html/all/latest.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  perl-generators
# /oreon:deps
%description
Code2HTML converts a program source code to syntax highlighted HTML.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
iconv -f iso8859-1 -t utf-8 %{name}.1 > %{name}.1.conv && mv -f %{name}.1.conv %{name}.1

%build

%install
mkdir -p %{buildroot}%{_bindir}
install -p -m 755 %{name} %{buildroot}%{_bindir}/
mkdir -p %{buildroot}%{_mandir}/man1
install -p -m 644 %{name}.1 %{buildroot}%{_mandir}/man1/
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
