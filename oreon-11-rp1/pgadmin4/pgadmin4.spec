%global source0_hash ca0dc0af7ede0f399c82a67587294761410fd136f32635f2c100623d117172c4
%ifnarch %{qt6_qtwebengine_arches}
%global debug_package %{nil}
%endif
Name:           pgadmin4
Version:        9.18
Release:        1%{?dist}
Summary:        Administration tool for PostgreSQL
ExcludeArch:    i686 armv7hl s390x ppc64le
License:        PostgreSQL AND MIT AND ISC AND Apache-2.0 AND BSD-2-Clause AND BSD-3-Clause AND CC0-1.0 AND 0BSD AND BlueOak-1.0.0 AND CC-BY-4.0 AND OFL-1.1 AND Unlicense AND Python-2.0.1 AND Apache-2.0 WITH LLVM-exception AND (WTFPL OR MIT) AND Zlib AND CC-BY-3.0
URL:            https://www.pgadmin.org/
Source0:        https://ftp.postgresql.org/pub/pgadmin/pgadmin4/v%{version}/source/pgadmin4-%{version}.tar.gz
Source1:        %{name}-%{version}-vendor.tar.xz
Source2:        %{name}-%{version}-vendor-licenses.txt
Source3:        %{name}-%{version}-yarn.lock
Source4:        pgadmin4-qt.cpp
Source5:        org.postgresql.pgadmin4.metainfo.xml
Source6:        pgadmin4-qt.svg
Source7:        pgadmin4.conf
Patch0:         pgadmin4_requirements.patch
Patch1:         pgadmin4_azure-mgmt-rdbms.patch
Patch2:         pgadmin4_sphinx_youtube.patch
Patch3:         pgadmin4_corepack.patch
Requires: python3dist(authlib) >= 1.5.2
Requires: python3dist(azure-identity) >= 1.17.1
Requires: python3dist(azure-mgmt-rdbms) >= 10.1.1
Requires: python3dist(azure-mgmt-resource) >= 24
Requires: python3dist(azure-mgmt-subscription) >= 3
Requires: python3dist(bcrypt) >= 4.3
Requires: python3dist(boto3) >= 1.42
Requires: python3dist(certifi) >= 2026.1.4
Requires: python3dist(cryptography) >= 46
Requires: python3dist(flask-babel) >= 4
Requires: python3dist(flask-compress) >= 1
Requires: python3dist(flask-login) >= 0
Requires: python3dist(flask-mail) >= 0
Requires: python3dist(flask-migrate) >= 4
Requires: python3dist(flask-paranoid) >= 0
Requires: python3dist(flask-security-too) >= 5.6.2
Requires: python3dist(flask-socketio) >= 5.6
Requires: python3dist(flask-sqlalchemy) >= 3.0.5
Requires: python3dist(flask-wtf) >= 1.2
Requires: python3dist(flask) >= 3.1
Requires: python3dist(google-api-python-client) >= 2
Requires: python3dist(google-auth-oauthlib) >= 1.2.4
Requires: python3dist(gssapi) >= 1.7.3
Requires: python3dist(jsonformatter) >= 0.3.4
Requires: python3dist(keyring) >= 25
Requires: python3dist(ldap3) >= 2
Requires: python3dist(libgravatar) >= 1
Requires: python3dist(paramiko) >= 3.5.1
Requires: python3dist(passlib) >= 1
Requires: python3dist(psutil) >= 7
Requires: python3dist(psycopg) >= 3.3.3
Requires: python3dist(pyotp) >= 2
Requires: python3dist(python-dateutil) >= 2
Requires: python3dist(pytz) >= 2025
Requires: python3dist(qrcode) >= 8
Requires: python3dist(setuptools) >= 80.10.2
Requires: python3dist(sqlalchemy) >= 2
Requires: python3dist(sqlparse) >= 0
Requires: python3dist(sshtunnel) >= 0
Requires: python3dist(typer) >= 0.24
Requires: python3dist(urllib3) >= 2.6
Requires: python3dist(user-agents) >= 2.2
Requires: python3dist(werkzeug) >= 3.1
Requires: python3dist(wtforms) >= 3.0.1
Requires:  python3-rich
Requires:  python3-libgravatar
Obsoletes: pgadmin3 < 1.23.0b-8
Provides:  pgadmin3 = %{version}-%{release}
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-pgadmin4 = %{version}-%{release}
# /oreon:deps
%description
pgAdmin is the most popular and feature rich Open Source administration and development
platform for PostgreSQL, the most advanced Open Source database in the world.

%package doc
Summary:       pgadmin4 documentation
BuildArch:     noarch
%description doc
pgadmin4 documentation.

%ifarch %{qt6_qtwebengine_arches}
%package qt
Summary:        Unofficial Qt runtime for pgadmin4
Requires:       %{name} = %{version}-%{release}
BuildRequires:  libappstream-glib
BuildRequires:  gcc-c++
BuildRequires:  desktop-file-utils
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtwebengine-devel
%description qt
This package contains an unofficial Qt runtime for pgadmin4.
%endif

%package httpd
Summary:        Apache/WSGI configuration for pgadmin4
Requires:       python3-mod_wsgi
Requires:       %{name} = %{version}-%{release}
%description httpd
This package contains the Apache/WSGI configuration for serving pgadmin4 from Apache.

%define lang_subpkg() \
%package langpack-%{1}\
Summary:       %{2} language data for %{name}\
BuildArch:     noarch\
Requires:      %{name} = %{version}-%{release}\
Supplements:   (%{name} = %{version}-%{release} and langpacks-%{1})\
\
%description langpack-%{1}\
%{2} language data for %{name}.\
\
%prep

%setup -q -a1
%autopatch -M99 -p1

sed -i 's|Exec=.*|Exec=%{_bindir}/%{name}-qt|' pkg/linux/%{name}.desktop
cp -a %{SOURCE2} .

%build

(
cd web
cp -a %{SOURCE3} yarn.lock
YARN_CACHE_FOLDER="$PWD/../.package-cache" yarn install --offline
yarn run bundle
rm -rf node_modules
)
%ifarch %{qt6_qtwebengine_arches}
g++ -o %{name}-qt %{SOURCE4} %{optflags} $(pkg-config --cflags --libs Qt6Core Qt6Widgets Qt6Network Qt6WebEngineCore Qt6WebEngineWidgets)
%endif
make docs PYTHON=%{__python3} SPHINXBUILD=sphinx-build
%install
mkdir -p %{buildroot}%{_prefix}/lib/
cp -a web %{buildroot}%{_prefix}/lib/%{name}
cat > %{buildroot}%{_prefix}/lib/%{name}/config_local.py <<EOF
from config import *
HELP_PATH = '%{_defaultdocdir}/%{name}/html/'
EOF
%ifarch %{qt6_qtwebengine_arches}
for size in 16 32 48 64 128; do
    install -Dpm 0644 pkg/linux/%{name}-${size}x${size}.png %{buildroot}%{_datadir}/icons/hicolor/${size}x${size}/apps/%{name}.png
done
install -Dpm 0755 %{name}-qt %{buildroot}%{_bindir}/%{name}-qt
install -Dpm 0644 pkg/linux/%{name}.desktop %{buildroot}%{_datadir}/applications/%{name}.desktop
install -Dpm 0644 %{SOURCE5} %{buildroot}%{_metainfodir}/org.postgresql.pgadmin4.metainfo.xml
install -Dpm 0644 %{SOURCE6} %{buildroot}%{_datadir}/pgadmin4-qt/pgadmin4-qt.svg
%endif
mkdir -p %{buildroot}%{_localstatedir}/lib/pgadmin
mkdir -p %{buildroot}%{_localstatedir}/log/pgadmin
install -Dpm 0644 %{SOURCE7} %{buildroot}%{_sysconfdir}/httpd/conf.d/pgadmin4.conf
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%ifarch %{qt6_qtwebengine_arches}
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/org.postgresql.pgadmin4.metainfo.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
%endif
%files
%files -n pgadmin4-doc -f %{oreon_filedir}/pgadmin4-doc.list
%files -n pgadmin4-httpd -f %{oreon_filedir}/pgadmin4-httpd.list
%files -n pgadmin4-langpack-cs -f %{oreon_filedir}/pgadmin4-langpack-cs.list
%files -n pgadmin4-langpack-de -f %{oreon_filedir}/pgadmin4-langpack-de.list
%files -n pgadmin4-langpack-es -f %{oreon_filedir}/pgadmin4-langpack-es.list
%files -n pgadmin4-langpack-fr -f %{oreon_filedir}/pgadmin4-langpack-fr.list
%files -n pgadmin4-langpack-it -f %{oreon_filedir}/pgadmin4-langpack-it.list
%files -n pgadmin4-langpack-ja -f %{oreon_filedir}/pgadmin4-langpack-ja.list
%files -n pgadmin4-langpack-ko -f %{oreon_filedir}/pgadmin4-langpack-ko.list
%files -n pgadmin4-langpack-pl -f %{oreon_filedir}/pgadmin4-langpack-pl.list
%files -n pgadmin4-langpack-ru -f %{oreon_filedir}/pgadmin4-langpack-ru.list

%changelog

%autochangelog
