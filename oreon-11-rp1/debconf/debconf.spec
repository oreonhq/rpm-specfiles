%global source0_hash 18f3f43924ccc870be483d7c5f1a9be59e51ae1da403059d654666b5a175bf15

%if 0%{?rhel} >= 10
    %bcond_with gnome
%else
    %bcond_without gnome
%endif

Name:           debconf
Version:        1.5.91
Release:        7%{?dist}
Summary:        Debian configuration management system

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://tracker.debian.org/pkg/debconf
Source0:        https://ftp.debian.org/debian/pool/main/d/%{name}/%{name}_%{version}.tar.xz
BuildArch:      noarch

#Build-Depends: debhelper-compat (= 12), dh-exec, dh-python, po-debconf, po4a (>= 0.23)
#Build-Depends-Indep: perl (>= 5.10.0-16), python3 (>= 3.1.2-8), gettext (>= 0.13), libintl-perl
BuildRequires:  make
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  po4a >= 0.23
BuildRequires:  gettext >= 0.13
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter

# Required in Debconf/Encoding.pm
# to test frontends : dpkg-reconfigure --frontend=kde tzdata
Requires:       perl(Text::Iconv)
Requires:       perl(Text::WrapI18N)
Requires:       perl(Text::CharWidth)
# Required in Debconf/Gettext.pm
Requires:       perl(Locale::gettext)

Obsoletes:      debconf-kde < 1.5.69-5

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
#make install-python3 prefix=%{buildroot}
install -d %{buildroot}%{python3_sitelib}
install -m 0644 debconf.py  %{buildroot}%{python3_sitelib}

make install-rest prefix=%{buildroot}

# Add /var/cache/debconf and initial contents
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

# Base and i18n man pages
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

# Doc foo
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

# Utils man pages
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

# Fix sbin merge for all releases
%if "%{_sbindir}" == "%{_bindir}"
     mkdir -p %{buildroot}%{_bindir}
     mv %{buildroot}/usr/sbin/* %{buildroot}%{_bindir}
%endif

%find_lang debconf

%files
%doc doc/README doc/EXAMPLES doc/CREDITS doc/README.translators doc/README.LDAP doc/TODO
%doc debian/changelog debian/README.Debian
%license debian/copyright
%config(noreplace) %{_sysconfdir}/debconf.conf
%{_bindir}/debconf
%{_bindir}/debconf-apt-progress
%{_bindir}/debconf-communicate
%{_bindir}/debconf-copydb
%{_bindir}/debconf-escape
%{_bindir}/debconf-set-selections
%{_bindir}/debconf-show
%{_sbindir}/dpkg-preconfigure
%{_sbindir}/dpkg-reconfigure
%{perl_vendorlib}/Debconf
%{perl_vendorlib}/Debian
%{_datadir}/%{name}
%{_mandir}/man1/debconf-apt-progress.1*
%{_mandir}/man1/debconf-communicate.1*
%{_mandir}/man1/debconf-copydb.1*
%{_mandir}/man1/debconf-escape.1*
%{_mandir}/man1/debconf-set-selections.1*
%{_mandir}/man1/debconf-show.1*
%{_mandir}/man1/debconf.1*
%{_mandir}/man8/dpkg-preconfigure.8*
%{_mandir}/man8/dpkg-reconfigure.8*
%{_datadir}/pixmaps/debian-logo.png
%{_var}/cache/%{name}
%exclude %{perl_vendorlib}/Debconf/Element/Gnome*
%exclude %{perl_vendorlib}/Debconf/FrontEnd/Gnome*
%exclude %{perl_vendorlib}/Debconf/DbDriver/LDAP.pm

%files LDAP
%doc doc/README.LDAP
%{perl_vendorlib}/Debconf/DbDriver/LDAP.pm

%if %{with gnome}
%files gnome
%{perl_vendorlib}/Debconf/Element/Gnome*
%{perl_vendorlib}/Debconf/FrontEnd/Gnome*
%endif

%files doc -f man-doc.lang
%doc samples/
%license debian/copyright
%doc doc/debconf.schema
%doc doc/hierarchy.txt
%doc doc/namespace.txt
%doc doc/passthrough.txt
%{_mandir}/man3/confmodule.3*
%{_mandir}/man5/debconf.conf.5*
%{_mandir}/man7/debconf-devel.7*
%{_mandir}/man7/debconf.7*

%files i18n -f man-i18n.lang -f debconf.lang
%doc debian/changelog debian/copyright debian/README.Debian

%files utils -f man-utils.lang
%doc debian/changelog debian/copyright debian/README.Debian
%{_bindir}/debconf-get-selections
%{_bindir}/debconf-getlang
%{_bindir}/debconf-loadtemplate
%{_bindir}/debconf-mergetemplate
%{_mandir}/man1/debconf-get-selections.1*
%{_mandir}/man1/debconf-getlang.1*
%{_mandir}/man1/debconf-loadtemplate.1*
%{_mandir}/man1/debconf-mergetemplate.1*

%files -n python%{python3_pkgversion}-%{name}
%{python3_sitelib}/debconf.py
%{python3_sitelib}/__pycache__/debconf.*

%changelog
%autochangelog
