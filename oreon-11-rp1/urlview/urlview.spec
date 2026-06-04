%global source0_hash none

%global gitdate 20131022
%global gitfullrev 08767aa863cd27d1755ba0aff65b8cc1a0c1446a
%global gitrev 08767a
Name:           urlview
Version:        0.9
Release:        41.%{gitdate}git%{gitrev}%{?dist}
Summary:        URL extractor/launcher

License:        GPL-2.0-only AND GPL-2.0-or-later AND LGPL-2.0-or-later
URL:            https://github.com/sigpipe/urlview
Source0:        https://github.com/sigpipe/urlview/archive/refs/tags/%{gitrev}.tar.gz#/urlview-%{gitrev}.tar.gz

BuildRequires: make
BuildRequires:  gcc
BuildRequires:  ncurses-devel

# mutt packages before 5:1.5.16-2 included urlview
Conflicts:      mutt < 5:1.5.16-2

Patch1:        urlview-default.patch

%description
urlview is a screen oriented program for extracting URLs from text
files and displaying a menu from which you may launch a command to
view a specific item.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n %{name}-%{gitfullrev}
%patch -P1 -p1 -b .default

%build
%configure
make %{?_smp_mflags}

%install
mkdir -p $RPM_BUILD_ROOT{%{_sysconfdir},%{_bindir},%{_mandir}/man{1,5}}
install -p -m644 urlview.conf.suse $RPM_BUILD_ROOT%{_sysconfdir}/urlview.conf
install -p urlview url_handler.sh $RPM_BUILD_ROOT%{_bindir}
install -p -m644 urlview.man $RPM_BUILD_ROOT%{_mandir}/man1/urlview.1
echo '.so man1/urlview.1' > $RPM_BUILD_ROOT%{_mandir}/man5/urlview.conf.5
echo '.so man1/urlview.1' > $RPM_BUILD_ROOT%{_mandir}/man1/url_handler.sh.1

%files
%doc AUTHORS ChangeLog COPYING README sample.urlview
%config(noreplace) %{_sysconfdir}/urlview.conf
%{_bindir}/urlview
%{_bindir}/url_handler.sh
%{_mandir}/man1/urlview.1*
%{_mandir}/man1/url_handler.sh.1*
%{_mandir}/man5/urlview.conf.5*

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.9-41.20131022git08767a
- Import
