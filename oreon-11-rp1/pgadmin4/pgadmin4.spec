%global source0_hash none

%ifnarch %{qt6_qtwebengine_arches}
# No useful debug package unless qt frontend is built (see %%package qt below)
%global debug_package %{nil}
%endif

Name:           pgadmin4
# NOTE: Also regenerate requires as indicated below when updating!
# Verify Patch4 on next update
Version:        9.13
Release:        1%{?dist}
Summary:        Administration tool for PostgreSQL

# i686, armv7hl: The webpack terser plugin aborts with JS heap memory exhaustion on these arches
# s390x: wasm aborts with RuntimeError: memory access out of bounds when attempting to build webfonts-loader
# ppc64le: wasm aborts with RuntimeError: float unrepresentable in integer range
ExcludeArch:    i686 armv7hl s390x ppc64le

# PostgreSQL ist the main license, rest the bundled JS code (see %%{name}-%%{version}-vendor-licenses.txt)
License:        PostgreSQL AND MIT AND ISC AND Apache-2.0 AND BSD-2-Clause AND BSD-3-Clause AND CC0-1.0 AND 0BSD AND BlueOak-1.0.0 AND CC-BY-4.0 AND OFL-1.1 AND Unlicense AND Python-2.0.1 AND Apache-2.0 WITH LLVM-exception AND (WTFPL OR MIT) AND Zlib AND CC-BY-3.0
URL:            https://www.pgadmin.org/
Source0:        https://ftp.postgresql.org/pub/pgadmin/pgadmin4/v%{version}/source/pgadmin4-%{version}.tar.gz

# ./prepare_vendor.sh
Source1:        %{name}-%{version}-vendor.tar.xz
Source2:        %{name}-%{version}-vendor-licenses.txt
Source3:        %{name}-%{version}-yarn.lock

# Unofficial qt runtime
Source4:        pgadmin4-qt.cpp
Source5:        org.postgresql.pgadmin4.metainfo.xml
Source6:        pgadmin4-qt.svg

# Apache/WSGI config
Source7:        pgadmin4.conf

# Patch requirements for Fedora compat, generate via ./adjust_requirements.py
Patch0:         pgadmin4_requirements.patch
# Fix python-azure-mgmt-rdbms-10.2.0~b5+ compatibility
Patch1:         pgadmin4_azure-mgmt-rdbms.patch
# Drop requirement on unpackaged python-sphinxcontrib-youtube
Patch2:         pgadmin4_sphinx_youtube.patch
# Drop packageManager field from package.json to avoid yarn complaining about corepack
Patch3:         pgadmin4_corepack.patch

# For docs
BuildRequires:  glibc-langpack-en
BuildRequires:  python3-devel
BuildRequires:  python3-keyring
BuildRequires:  python3-sphinx
BuildRequires:  python3-setuptools
BuildRequires:  yarnpkg

# For node dependencies
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libpng-devel
BuildRequires:  libtool

# Printed by ./adjust_requirements.py (which also generates pgadmin4_requirements.patch)
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

# Undeclared dependencies
Requires:  python3-rich
Requires:  python3-libgravatar

Obsoletes: pgadmin3 < 1.23.0b-8
Provides:  pgadmin3 = %{version}-%{release}

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
%files langpack-%{1}\
%{_prefix}/lib/%{name}/pgadmin/translations/%{1}/

%lang_subpkg cs Czech
%lang_subpkg de German
%lang_subpkg es Spanish
%lang_subpkg fr French
%lang_subpkg it Italian
%lang_subpkg ja Japanese
%lang_subpkg ko Korean
%lang_subpkg pl Polish
%lang_subpkg ru Russian

%generate_buildrequires
%pyproject_buildrequires -N requirements.txt

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

# Local config
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

# Apache/WSGI config
mkdir -p %{buildroot}%{_localstatedir}/lib/pgadmin
mkdir -p %{buildroot}%{_localstatedir}/log/pgadmin
install -Dpm 0644 %{SOURCE7} %{buildroot}%{_sysconfdir}/httpd/conf.d/pgadmin4.conf

%check
%ifarch %{qt6_qtwebengine_arches}
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/org.postgresql.pgadmin4.metainfo.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
%endif

%files
%license LICENSE %{name}-%{version}-vendor-licenses.txt
%doc README.md
%{_prefix}/lib/%{name}
# Packaged by separate langpack subpackages
%exclude %{_prefix}/lib/%{name}/pgadmin/translations/*

%files doc
%license LICENSE %{name}-%{version}-vendor-licenses.txt
%doc docs/en_US/_build/html

%ifarch %{qt6_qtwebengine_arches}
%files qt
%{_bindir}/%{name}-qt
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/pgadmin4-qt/
%{_metainfodir}/org.postgresql.pgadmin4.metainfo.xml
%endif

%files httpd
%config(noreplace) %{_sysconfdir}/httpd/conf.d/pgadmin4.conf
%attr(0700,apache,apache) %dir %{_localstatedir}/lib/pgadmin
%attr(0700,apache,apache) %dir %{_localstatedir}/log/pgadmin

%changelog
%autochangelog
