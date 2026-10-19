%global source01_hash a670a15c5bb4acfc9161da76cbc955898d981293a17e1ac330b5e6f5e051add7
%global source0_hash none
%global source00_hash ce294673c634faf38d8d83b18fa0003f73a0e4d90160b9faa474689543332d42
%{!?tetex:%global tetex 1}
%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}
%global _vendorperllibdir %{_datadir}/perl5/vendor_perl
Summary:        A text formatting package based on SGML
Name: linuxdoc-tools
Version: 0.9.85
Release:        1%{?dist}
License: X11-distribute-modifications-variant
Source00:        https://snapshot.debian.org/archive/debian/20241101T000000Z/pool/main/l/linuxdoc-tools/%{name}_%{version}.orig.tar.gz
Source01:        https://snapshot.debian.org/archive/debian/20241101T000000Z/pool/main/l/linuxdoc-tools/%{name}_%{version}.orig.tar.gz.asc
Patch01: 0001-downstream-Changed-default-papersize-to-letter.patch
Patch02: 0002-downstream-Added-fix-to-have-lib64-in-perl-path-on-6.patch
Url: http://packages.qa.debian.org/l/linuxdoc-tools.html
Requires: jade gawk groff
Requires(post): %{_bindir}/texconfig-sys
Requires(postun): %{_bindir}/texconfig-sys
%if %{tetex}
Requires: tex(latex)
%endif
Obsoletes: sgml-tools < %{version}-%{release}
Obsoletes: linuxdoc-sgml < %{version}-%{release}
Provides: sgml-tools = %{version}-%{release}
Provides: linuxdoc-sgml = %{version}-%{release}
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  flex
BuildRequires:  flex-static
BuildRequires:  gawk
BuildRequires:  gcc
BuildRequires:  git
BuildRequires:  groff
BuildRequires:  jade
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  sgml-common
BuildRequires:  texinfo
# /oreon:deps
%description
Linuxdoc-tools is a text formatting suite based on SGML (Standard
Generalized Markup Language), using the LinuxDoc document type.
Linuxdoc-tools allows you to produce LaTeX, HTML, GNU info, LyX, RTF,
plain text (via groff), and other format outputs from a single SGML
source.  Linuxdoc-tools is intended for writing technical software
documentation.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
test "%{source00_hash}" = "none" || { f="%{SOURCE00}"; test -f "$f" || { echo "oreon: missing Source00 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source00_hash}" || { echo "oreon: Source00 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

autoreconf -i
%configure --with-installed-nsgmls --with-installed-iso-entities --disable-docs
pushd entity-map
autoconf
%configure --enable-docs pdf
popd
make OPTIMIZE="$RPM_OPT_FLAGS" %{?_smp_mflags}
perl -pi -e 's,\$main::prefix/share/sgml/iso-entities-8879.1986/iso-entities.cat,/usr/share/sgml/sgml-iso-entities-8879.1986/catalog,' \
           perl5lib/LinuxDocTools.pm
%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_vendorperllibdir}
make install DESTDIR=$RPM_BUILD_ROOT perl5libdir=%{_vendorperllibdir}
[ $RPM_BUILD_ROOT%{_docdir}/%{name} = $RPM_BUILD_ROOT%{_pkgdocdir} ] \
           || mv $RPM_BUILD_ROOT%{_docdir}/%{name} $RPM_BUILD_ROOT%{_pkgdocdir}
perl -pi -e 's,/usr/share/sgml/iso-entities-8879.1986/iso-entities.cat,\$main::prefix/share/sgml/sgml-iso-entities-8879.1986/catalog,' \
           $RPM_BUILD_ROOT%{_vendorperllibdir}/LinuxDocTools.pm
mkdir -p $RPM_BUILD_ROOT%{_pkgdocdir}/sgmls-1.1
cp -p sgmls-1.1/LICENSE $RPM_BUILD_ROOT%{_pkgdocdir}/sgmls-1.1/LICENSE
mkdir -p $RPM_BUILD_ROOT%{_pkgdocdir}/iso-entities
cp -p iso-entities/COPYING $RPM_BUILD_ROOT%{_pkgdocdir}/iso-entities/COPYING
mkdir -p $RPM_BUILD_ROOT%{_pkgdocdir}/entity-map
cp -p entity-map/COPYING $RPM_BUILD_ROOT%{_pkgdocdir}/entity-map/COPYING
cp -p COPYING $RPM_BUILD_ROOT%{_pkgdocdir}/
rm -f $RPM_BUILD_ROOT%{_datadir}/%{name}/epsf.*
rm -f $RPM_BUILD_ROOT%{_datadir}/%{name}/url.sty
install -d $RPM_BUILD_ROOT%{_datadir}/texmf/tex/latex/misc
mv $RPM_BUILD_ROOT%{_datadir}/%{name}/*.sty \
  $RPM_BUILD_ROOT%{_datadir}/texmf/tex/latex/misc
%oreon_autofiles main

%post

%{_bindir}/texconfig-sys rehash 2> /dev/null || :
exit 0
%postun

%{_bindir}/texconfig-sys rehash 2> /dev/null || :
exit 0
%files -f %{oreon_filedir}/main.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.9.85-3
- Import
