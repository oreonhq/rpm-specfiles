%global source0_hash 1f7a9b9c1c9f47dd46384ffd0bde77b3300da90fc861aa7d37ad9467505be8b9
    %bcond_without gnome
Name:           debconf
Version:        1.5.92.git
Release:        1%{?dist}
Summary:        Debian configuration management system
License:        LicenseRef-Callaway-BSD
URL:            https://tracker.debian.org/pkg/debconf
Source0:        https://ftp.debian.org/debian/pool/main/d/%{name}/%{name}_%{version}.tar.xz
BuildArch:      noarch
Requires:       perl(Text::Iconv)
Requires:       perl(Text::WrapI18N)
Requires:       perl(Text::CharWidth)
Requires:       perl(Locale::gettext)
Obsoletes:      debconf-kde < 1.5.69-5
# oreon:deps
BuildRequires:  gettext
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  po4a
BuildRequires:  python3-devel
# /oreon:deps
%description
Debconf is a configuration management system for Debian
packages. Packages use Debconf to ask questions when
they are installed.

%package gnome
Summary:       GNOME frontend for debconf
Requires:      %{name} = %{version}-%{release}
%description gnome
This package contains the GNOME frontend for debconf.

%package LDAP
Summary:       Experimental LDAP driver for debconf
Requires:      %{name} = %{version}-%{release}
%description LDAP
This package contains an experimental database driver to provide LDAP support
for debconf

%package doc
Summary:        Debconf documentation
Requires:       %{name} = %{version}-%{release}
%description doc
This package contains lots of additional documentation for Debconf,
including the debconf user's guide, documentation about using
different backend databases via the /etc/debconf.conf file, and a
developer's guide to debconf.

%package i18n
Summary:        Full internationalization support for debconf
Requires:       %{name} = %{version}-%{release}
%description i18n
This package provides full internationalization for debconf,
including translations into all available languages, support
for using translated debconf templates, and support for
proper display of multibyte character sets.

%package utils
Summary:        This package contains some small utilities for debconf developers
Requires:       %{name} = %{version}-%{release}
%description utils
This package contains some small utilities for debconf developers.

%package -n python%{python3_pkgversion}-%{name}
Summary:        Python3 for debconf
%{?python_provide:%python_provide python%{python3_pkgversion}-%{name}}
%description -n python%{python3_pkgversion}-%{name}
This package contains the python3 for debconf.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n work

%build

%make_build
%install
make install-utils prefix=%{buildroot}
make install-i18n prefix=%{buildroot}
install -d %{buildroot}%{python3_sitelib}
install -m 0644 debconf.py  %{buildroot}%{python3_sitelib}
make install-rest prefix=%{buildroot}
mkdir -p %{buildroot}/%{_var}/cache/%{name}
touch %{buildroot}/%{_var}/cache/%{name}/config.dat
touch %{buildroot}/%{_var}/cache/%{name}/passwords.dat
touch %{buildroot}/%{_var}/cache/%{name}/templates.dat
mkdir -p \
        %{buildroot}/%{perl_vendorlib} \
        %{buildroot}/%{_mandir}/man{1,3,5,7,8} \
        %{buildroot}/%{_mandir}/de/man{1,3,5,7,8} \
        %{buildroot}/%{_mandir}/fr/man{1,3,5,7,8} \
        %{buildroot}/%{_mandir}/ru/man{1,3,5,7,8} \
        %{buildroot}/%{_mandir}/pt_BR/man{1,3,8}
chmod 755 %{buildroot}/%{_datadir}/%{name}/confmodule*
for man in \
        "debconf-apt-progress" \
        "debconf-communicate" \
        "debconf-copydb" \
        "debconf-escape" \
        "debconf-set-selections" \
        "debconf-show" \
        "debconf" \
        "dpkg-preconfigure" \
        "dpkg-reconfigure"; do
    for level in 1 8; do
        for lang in de fr pt_BR ru; do
            if test -f doc/man/gen/$man.$lang.$level; then
                short_lang=`echo "$lang" | sed 's/_.*//'`
                install -m 644 doc/man/gen/$man.$lang.$level %{buildroot}/%{_mandir}/$lang/man$level/$man.$level
                echo "%lang($short_lang) %{_mandir}/$lang/man$level/$man.$level*" >> "man-i18n.lang"
            fi
        done
        test -f doc/man/gen/$man.$level && \
            install -m 644 doc/man/gen/$man.$level %{buildroot}/%{_mandir}/man$level/$man.$level
    done
done
for man in \
        "Debconf::Client::ConfModule" \
        "confmodule" \
        "debconf.conf" \
        "debconf-devel" \
        "debconf"; do
    for level in 3 5 7; do
        for lang in de fr pt_BR ru; do
            if test -f doc/man/$man.$lang.$level*; then
                short_lang=`echo "$lang" | sed 's/_.*//'`
                install -m 644 doc/man/$man.$lang.$level* %{buildroot}/%{_mandir}/$lang/man$level/$man.$level
                echo "%lang($short_lang) %{_mandir}/$lang/man$level/$man.$level*" >> "man-doc.lang"
            fi
        done
        test -f doc/man/$man.$level && \
            install -m 644 doc/man/$man.$level %{buildroot}/%{_mandir}/man$level/$man.$level
    done
done
for man in get-selections \
            getlang \
            loadtemplate \
            mergetemplate; do
    for lang in de fr pt_BR ru; do
        short_lang=`echo "$lang" | sed 's/_.*//'`
        if test -f doc/man/gen/debconf-$man.$lang.1; then
            install -m 644 doc/man/gen/debconf-$man.$lang.1 %{buildroot}/%{_mandir}/$lang/man1/debconf-$man.1
            echo "%lang($short_lang) %{_mandir}/$lang/man1/debconf-$man.1*" >> "man-utils.lang"
        fi
    done
    test -f doc/man/gen/debconf-$man.1 && \
        install -m 644 doc/man/gen/debconf-$man.1 %{buildroot}/%{_mandir}/man1/debconf-$man.1
done
%if "%{_sbindir}" == "%{_bindir}"
     mkdir -p %{buildroot}%{_bindir}
     mv %{buildroot}/usr/sbin/* %{buildroot}%{_bindir}
%endif
%find_lang debconf
%oreon_autofiles debconf-gnome usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles debconf-LDAP usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles debconf-doc usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles debconf-i18n usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles debconf-utils usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles python3-debconf usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n debconf-gnome -f %{oreon_filedir}/debconf-gnome.list
%files -n debconf-LDAP -f %{oreon_filedir}/debconf-LDAP.list
%files -n debconf-doc -f %{oreon_filedir}/debconf-doc.list
%files -n debconf-i18n -f %{oreon_filedir}/debconf-i18n.list
%files -n debconf-utils -f %{oreon_filedir}/debconf-utils.list
%files -n python3-debconf -f %{oreon_filedir}/python3-debconf.list

%changelog

%autochangelog
