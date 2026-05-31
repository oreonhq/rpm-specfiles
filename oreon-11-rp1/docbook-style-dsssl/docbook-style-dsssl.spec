%global source0_hash d5a199024a5fe0862bfaff9e3533817cd8d08bddf3cdfb5bfe6088cbb2cd62b3

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
Source0:        http://prdownloads.sourceforge.net/docbook/docbook-dsssl-%{version}.tar.gz
Source1: %{name}.Makefile


%description
These DSSSL stylesheets allow to convert any DocBook document to another
printed (for example, RTF or PostScript) or online (for example, HTML) format.
They are highly customizable.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
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
