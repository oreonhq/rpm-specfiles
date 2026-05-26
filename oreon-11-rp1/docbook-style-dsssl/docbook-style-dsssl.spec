Name: docbook-style-dsssl
Version: 1.79
Release: 44%{?dist}

Summary: Norman Walsh's modular stylesheets for DocBook

License: LicenseRef-DMIT
URL: http://docbook.sourceforge.net/
BuildRequires: perl-generators
BuildRequires: make

Requires: docbook-dtds
Requires: openjade
Requires: sgml-common
Requires(post): sgml-common
Requires(preun): sgml-common

BuildArch: noarch
Source0: http://prdownloads.sourceforge.net/docbook/docbook-dsssl-%{version}.tar.gz
Source1: %{name}.Makefile
# oreon url source checksums begin
%global source0_sha256 d5a199024a5fe0862bfaff9e3533817cd8d08bddf3cdfb5bfe6088cbb2cd62b3
%global source0_file docbook-dsssl-1.79.tar.gz
# oreon url source checksums end


%description
These DSSSL stylesheets allow to convert any DocBook document to another
printed (for example, RTF or PostScript) or online (for example, HTML) format.
They are highly customizable.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/docbook-dsssl-1.79.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "d5a199024a5fe0862bfaff9e3533817cd8d08bddf3cdfb5bfe6088cbb2cd62b3" || { echo "oreon: Source0 SHA256 mismatch for docbook-dsssl-1.79.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%setup -q -n docbook-dsssl-%{version}
cp %{SOURCE1} Makefile


%build

%install
DESTDIR=$RPM_BUILD_ROOT
make install BINDIR=$DESTDIR/usr/bin DESTDIR=$DESTDIR/usr/share/sgml/docbook/dsssl-stylesheets-%{version} MANDIR=$DESTDIR%{_mandir}
cd ..
ln -s dsssl-stylesheets-%{version} $DESTDIR/usr/share/sgml/docbook/dsssl-stylesheets

%files
%doc BUGS README ChangeLog WhatsNew
/usr/bin/collateindex.pl
%{_mandir}/man1/collateindex.pl.1*
/usr/share/sgml/docbook/dsssl-stylesheets-%{version}
/usr/share/sgml/docbook/dsssl-stylesheets


%post
for centralized in /etc/sgml/*-docbook-*.cat
do
  /usr/bin/install-catalog --add $centralized \
    /usr/share/sgml/docbook/dsssl-stylesheets-%{version}/catalog \
    > /dev/null 2>/dev/null
done


%preun
if [ "$1" = "0" ]; then
  for centralized in /etc/sgml/*-docbook-*.cat
  do
    /usr/bin/install-catalog --remove $centralized /usr/share/sgml/docbook/dsssl-stylesheets-%{version}/catalog > /dev/null 2>/dev/null
  done
fi
exit 0

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.79-44
- Prepare for Oreon 11 (RP1)
