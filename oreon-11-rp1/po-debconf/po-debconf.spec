%global source0_hash 852c27bba64d435364252aabe440412a71a175055a0cb48b9458a8b02586f640
%global	posttag	nmu1
%global	release_posttag %{?posttag:.%{posttag}}
%global	tarball_posttag %{?posttag:+%{posttag}}
%global	debian_fqn %{name}_%{version}%{tarball_posttag}
%bcond check 1
Name:		po-debconf
Version:	1.0.22
Release:        1%{?dist}
Summary:        Tool for managing templates file translations with gettext
License:	GPL-2.0-or-later
URL:		https://tracker.debian.org/pkg/po-debconf
Source0:        https://ftp.debian.org/debian/pool/main/p/%{name}/%{name}_%{version}+%{posttag}.tar.xz
BuildArch:	noarch
%if %{with check}
%endif
Requires:	perl-interpreter
Requires:	intltool
Requires:	gettext
Recommends:	perl(Compress::Zlib)
Recommends:	perl(Mail::Sendmail)
Recommends:	perl(Mail::Box::Manager)
# oreon:deps
BuildRequires:  /usr/bin/pod2html
BuildRequires:  debconf
BuildRequires:  dpkg-dev
BuildRequires:  intltool
BuildRequires:  make
BuildRequires:  perl(Test)
BuildRequires:  perl(Test::Harness)
BuildRequires:  perl-generators
BuildRequires:  po4a
# /oreon:deps
%description
This package is an alternative to debconf-utils, and provides
tools for managing translated debconf templates files with
common gettext utilities.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{version}%{tarball_posttag}

# Fix upstream
chmod -x COPYING

%build

%make_build
%install
mkdir -p \
	%{buildroot}/%{_bindir} \
	%{buildroot}/%{_datadir}/%{name}/
for prog in debconf-gettextize debconf-updatepo po2debconf podebconf-display-po podebconf-report-po; do
	install -pm 755 $prog %{buildroot}/%{_bindir}
done
rm -rf doc/vi
for lang_man in `find doc/ -name "*.1" -exec dirname {} \; | sort -u`; do
	lang_id=$(basename $lang_man | sed -e 's/en//g')
	mkdir -p %{buildroot}/%{_mandir}/man1/
	mkdir -p "%{buildroot}/%{_mandir}/$lang_id/man1"
	for man in $lang_man/*.1; do
		dest_name=$(basename $man | sed -e "s/\.$lang_id\././")
		install -pm 644 "$man" "%{buildroot}/%{_mandir}/$lang_id/man1/$dest_name"
	done
done
install -pm 644 encodings %{buildroot}%{_datadir}/%{name}/
install -pm 644 pot-header %{buildroot}%{_datadir}/%{name}/
cp -a podebconf-report-po_templates/ %{buildroot}%{_datadir}/%{name}/templates
ln -s ../bin %{buildroot}%{_datadir}/intltool-debian
%find_lang po-debconf --without-mo --with-man --all-name
%oreon_autofiles main
%if %{with check}
%check

( cd ./tests && PODEBCONF_LIB=/usr/bin ./run.pl )
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
