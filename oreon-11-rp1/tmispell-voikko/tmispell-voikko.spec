%global source1_hash 1fd670885be6ebcefb05a4098556324411668d33a20120ebf44fcbdd23c45216
%global source0_hash 35bd2e3f7421d400df9f9637c92d9bb5bba6f6a7fc3bb0aa49a31b68e9b91f0d
%bcond_with enchant
Name:           tmispell-voikko
Version:        0.7.1
Release:        38%{?dist}
Summary:        An Ispell compatible front-end for spell-checking modules
License:        GPL-2.0-or-later
URL:            https://voikko.puimula.org/
Source0:        https://www.puimula.org/voikko-sources/%{name}/%{name}-%{version}.tar.gz
Source1:        https://www.puimula.org/voikko-sources/%{name}/%{name}-%{version}.tar.gz.asc
Source2:        gpgkey-AC5D65F10C8596D7E2DAE2633D309B604AE3942E.gpg
Patch0:         tmispell-voikko-0.7.1-glib-2.31-fix.patch
Patch1:         0001-redraw_minimenu-add-format-string.patch
%if %{with enchant}
%endif
# oreon:deps
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  glibmm24-devel
BuildRequires:  gnupg2
BuildRequires:  libvoikko-devel
BuildRequires:  make
BuildRequires:  ncurses-devel
# /oreon:deps
%description
Tmispell is an Ispell compatible front-end for spell-checking
modules. To do the actual spell-checking for Finnish language it uses
the spell-checking system Voikko.

%package -n 	enchant-voikko
Summary:        Voikko spellchecker support for Enchant
%description -n enchant-voikko
Voikko spellchecker support for Enchant.

# TODO: /usr/bin/ispell should be a symlink to /usr/bin/tmispell and the real
# ispell should be renamed to e.g. /usr/bin/ispell.real for KDE etc. to work.
# The other option would be to modify /usr/bin/ispell to call
# /usr/bin/tmispell when it's called with Finnish. If neither of these can be
# done, it's worth it to have /usr/bin/tmispell as a command line client for
# Voikko.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1

%build

%if %{with enchant}
%configure --disable-dependency-tracking
%else
%configure --disable-dependency-tracking --disable-enchant
%endif
make %{?_smp_mflags}
%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
%if %{with enchant}
find $RPM_BUILD_ROOT -name '*.a' -exec rm -f {} ';'
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'
rm $RPM_BUILD_ROOT%{_libdir}/enchant/libenchant_voikko.so.1 \
   $RPM_BUILD_ROOT%{_libdir}/enchant/libenchant_voikko.so
mv $RPM_BUILD_ROOT%{_libdir}/enchant/libenchant_voikko.so.* \
   $RPM_BUILD_ROOT%{_libdir}/enchant/libenchant_voikko.so
%endif
sed -i -e 's/ispell.real/ispell/' tmispell.conf.example
install -Dpm 0644 tmispell.conf.example $RPM_BUILD_ROOT%{_sysconfdir}/tmispell.conf
%find_lang %{name}
%oreon_autofiles enchant-voikko usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n enchant-voikko -f %{oreon_filedir}/enchant-voikko.list

%changelog

%autochangelog
