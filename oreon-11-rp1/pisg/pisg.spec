%global source0_hash 979efdd489114c10360dff9c7c8fdc287c126508e65790dfd0d0aa6fdf7d7c3b
Name:           pisg
Version:        0.73
Release:        41%{?dist}
Summary:        IRC Statistics generator
License:        GPL-2.0-or-later
URL:            http://pisg.sourceforge.net/
Source0:        http://prdownloads.sourceforge.net/pisg/%{name}-%{version}.tar.gz
Patch0:         pisg-0.72-systemdirs.patch
BuildArch:      noarch
Requires:       perl(Text::Iconv)
%{?perl_default_filter}
# oreon:deps
BuildRequires:  perl-generators
# /oreon:deps
%description
Pisg is an IRC statistics generator. It takes IRC log-files and turns
them into nice looking stats.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1
for file in COPYING \
            README \
            $(find docs -type f) \
            $(find scripts -type f) \
            $(find modules -type f) \
            $(find gfx -type f) \
            $(find layout -type f)
do
    chmod 644 ${file}
done
sed -i 's/\r//' scripts/mirc2egg.sed

%install
install -p -D -m755 pisg %{buildroot}%{_bindir}/pisg
install -p -D -m644 pisg.cfg %{buildroot}%{_sysconfdir}/pisg.cfg
install -p -D -m644 lang.txt %{buildroot}%{_datadir}/pisg/lang.txt
cp -rp gfx %{buildroot}%{_datadir}/pisg/gfx
cp -rp layout %{buildroot}%{_datadir}/pisg/layout
install -p -D -m644 modules/Pisg.pm %{buildroot}%{perl_vendorlib}/Pisg.pm
cp -rp modules/Pisg %{buildroot}%{perl_vendorlib}/Pisg
install -p -D -m644 docs/pisg.1 %{buildroot}%{_mandir}/man1/pisg.1
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
