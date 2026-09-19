%global source0_hash 35bd2e3f7421d400df9f9637c92d9bb5bba6f6a7fc3bb0aa49a31b68e9b91f0d

# Building the Enchant Voikko provider is disabled by default because it should
# be included in Enchant 1.4.
# Pass '--with enchant' on rpmbuild command-line to enable it.
%bcond_with enchant

Name:           tmispell-voikko
Version:        0.7.1
Release:        38%{?dist}
Summary:        An Ispell compatible front-end for spell-checking modules

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://voikko.puimula.org/
Source0:        https://www.puimula.org/voikko-sources/%{name}/%{name}-%{version}.tar.gz
Source1:        https://www.puimula.org/voikko-sources/%{name}/%{name}-%{version}.tar.gz.asc
# Keyring created by running
# gpg2 --export --export-options export-minimal "AC5D 65F1 0C85 96D7 E2DA E263 3D30 9B60 4AE3 942E" > gpgkey-AC5D65F10C8596D7E2DAE2633D309B604AE3942E.gpg
# See https://voikko.puimula.org/sources.html
Source2:        gpgkey-AC5D65F10C8596D7E2DAE2633D309B604AE3942E.gpg
Patch0:         tmispell-voikko-0.7.1-glib-2.31-fix.patch
Patch1:         0001-redraw_minimenu-add-format-string.patch

BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  gnupg2
BuildRequires:  libvoikko-devel ncurses-devel gettext glibmm24-devel
%if %{with enchant}
BuildRequires: enchant-devel
%endif

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
# Remove static archive
find $RPM_BUILD_ROOT -name '*.a' -exec rm -f {} ';'
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'
# Remove the symlinks and move the library itself into a better name
rm $RPM_BUILD_ROOT%{_libdir}/enchant/libenchant_voikko.so.1 \
   $RPM_BUILD_ROOT%{_libdir}/enchant/libenchant_voikko.so
mv $RPM_BUILD_ROOT%{_libdir}/enchant/libenchant_voikko.so.* \
   $RPM_BUILD_ROOT%{_libdir}/enchant/libenchant_voikko.so
%endif
# Install the configuration file
sed -i -e 's/ispell.real/ispell/' tmispell.conf.example
install -Dpm 0644 tmispell.conf.example $RPM_BUILD_ROOT%{_sysconfdir}/tmispell.conf
# Fake Finnish dictionary for ispell clients. Commented out for now.
# These won't actually work for KDE etc. unless the binary is in
# /usr/bin/ispell (or /usr/bin/ispell calls tmispell). These files should always 
# be installed into %{_prefix}/lib/ispell/ even though it's an rpmlint error
# because my testing shows that KDE recognizes them from there but not from 
# /usr/share.
#install -dm 755 %{buildroot}%{_prefix}/lib/ispell
#touch %{buildroot}%{_prefix}/lib/ispell/suomi.{hash,aff}
%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS ChangeLog COPYING NEWS README README.fi
%config(noreplace) %{_sysconfdir}/tmispell.conf
%{_mandir}/man1/tmispell*
%{_mandir}/man5/tmispell*
%{_bindir}/tmispell
# Fake dictionary directory, commented out for now
#%{_prefix}/lib/ispell

%if %{with enchant}
%files -n enchant-voikko
%{_libdir}/enchant/libenchant_voikko.so
%endif

%changelog
%autochangelog
