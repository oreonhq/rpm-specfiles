%global source0_hash 948794a316aaecd13add60e17e476beae86644d066cb60171fc6b779f2df14b0

Name:           xmltoman
Version:        0.4
Release:        34%{?dist}
Summary:        Scripts for converting XML to roff or HTML

License:        GPL-2.0-or-later
URL:            http://sourceforge.net/projects/xmltoman/
Source0:        https://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Patch0:         xmltoman-0.3-timestamps.patch

BuildRequires: make
BuildRequires:  perl-generators
BuildRequires:  perl(XML::Parser)
BuildArch:      noarch

%description
This package provides xmltoman and xmlmantohtml scripts, to compile
the xml representation of manual page to either roff source, or HTML
(while providing the CSS stylesheet for eye-candy look). XSL stylesheet
for doing rougly the same job is provided.


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q
%patch -P0 -p1 -b .timestamps


%build
make %{?_smp_mflags}


%install
make install PREFIX=%{_prefix} DESTDIR=%{buildroot}
mkdir -p %{buildroot}%{_mandir}/man1
cp -p *.1 %{buildroot}%{_mandir}/man1


%files
%{_bindir}/xmltoman
%{_bindir}/xmlmantohtml
%{_datadir}/xmltoman
%{_mandir}/*/*
%doc COPYING README


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.4-34
- Prepare for Oreon 11 (RP1)
