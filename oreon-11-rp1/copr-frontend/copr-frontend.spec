%global source0_hash 5d39d32b24af2d513ba5927016a410746f74ffe43ca268ea086aa521ca1dcfa9

%bcond check 0
%bcond_with doc

# https://fedoraproject.org/wiki/Packaging:Guidelines#Packaging_of_Additional_RPM_Macros
%global macrosdir       %(d=%{_rpmconfigdir}/macros.d; [ -d $d ] || d=%{_sysconfdir}/rpm; echo $d)

%global copr_common_version 1.1.2

# Please bump the %%flavor_guard version every-time some incompatible change
# happens (since the last release) in %%flavor_files set of files.  Those files
# are basically replaced by third-party flavor providers, and any file removal,
# addition, movement or change will make the third-party flavor non-working.  By
# changing the version we make the package explicitly incompatible and
# third-party flavor providers are notified they have to update their packages,
# too.
%global flavor_guard      %name-flavor = 6
%global flavor_provides   Provides: %flavor_guard
%global flavor_files_list %_datadir/copr/copr-flavor-filelist
%global flavor_generator  %_datadir/copr/coprs_frontend/generate_colorscheme
%global staticdir         %_datadir/copr/coprs_frontend/coprs/static
%global templatedir       %_datadir/copr/coprs_frontend/coprs/templates

%global flavor_files                            \
%staticdir/header_background.png                \
%staticdir/favicon.ico                          \
%staticdir/copr_logo.png                        \
%staticdir/css/copr-flavor.css                  \
%templatedir/additional_token_info.html         \
%templatedir/project_info.html                  \
%templatedir/quick_enable.html                  \
%templatedir/user_meta.html                     \
%templatedir/homepage_header.html               \
%templatedir/documentation_cards.html           \
%templatedir/welcome.html                       \
%templatedir/contact_us.html                    \
%templatedir/sponsors.html

%global devel_files \
%flavor_generator

%define exclude_files() %{lua:
   macro = "%" .. rpm.expand("%1") .. "_files"
   x = rpm.expand(macro)
   for line in string.gmatch(x, "([^\\n]+)") do
       print("%exclude " .. line .. "\\n")
   end
}

Name:       copr-frontend
Version:    2.6.hotfix.4
Release:    1%{?dist}
Summary:    Frontend for Copr

License:    GPL-2.0-or-later
URL:        https://github.com/fedora-copr/copr

# Source is created by:
# git clone %%url && cd copr
# tito build --tgz --tag %%name-%%version-%%release
Source0:    %name-%version.tar.gz

BuildArch:  noarch

BuildRequires: systemd
BuildRequires: util-linux

%if %{with doc}
BuildRequires: epydoc
BuildRequires: graphviz
%endif

BuildRequires: python3-devel

%if %{with check}
BuildRequires: python3dist(alembic)
BuildRequires: python3dist(anytree)
BuildRequires: python3dist(click)
BuildRequires: python3dist(commonmark)
BuildRequires: python3dist(blinker)
BuildRequires: python3dist(beautifulsoup4)
BuildRequires: python3dist(copr-common) >= %copr_common_version
BuildRequires: python3dist(email-validator)
BuildRequires: python3dist(python-dateutil)
BuildRequires: python3dist(decorator)
BuildRequires: python3dist(flask)
BuildRequires: python3dist(templated-dictionary)
BuildRequires: python3dist(flask-caching)
BuildRequires: python3dist(flask-sqlalchemy)
BuildRequires: python3dist(flask-session)
BuildRequires: python3dist(flask-whooshee)
BuildRequires: python3dist(flask-wtf)
BuildRequires: python3dist(flask-restx)
BuildRequires: python3-gobject
BuildRequires: python3dist(html2text)
BuildRequires: python3dist(html5-parser)
BuildRequires: python3dist(humanize)
BuildRequires: python3dist(lxml)
BuildRequires: python3dist(markdown)
BuildRequires: python3dist(markupsafe)
BuildRequires: python3dist(munch)
BuildRequires: python3dist(netaddr)
BuildRequires: python3dist(pygments)
BuildRequires: python3dist(pylibravatar)
BuildRequires: python3dist(pytest)
BuildRequires: python3dist(redis)
BuildRequires: python3dist(requests)
BuildRequires: python3dist(sphinx)
BuildRequires: python3dist(sphinxcontrib-httpdomain)
BuildRequires: python3dist(whoosh)
BuildRequires: python3dist(wtforms) >= 2.2.1
BuildRequires: python3dist(python-ldap)
BuildRequires: python3dist(pyyaml)
BuildRequires: python3dist(backoff) >= 1.9.0
BuildRequires: python3dist(pygal)
BuildRequires: redis
BuildRequires: modulemd-tools >= 0.6
BuildRequires: python3dist(authlib)
%endif

Requires: crontabs
Requires: curl
Requires: httpd
Recommends: logrotate
Recommends: mod_auth_gssapi
Requires: redis

Requires: %flavor_guard

Requires: (copr-selinux if selinux-policy-targeted)
Recommends: fedora-messaging
Requires: js-jquery
Requires: python3dist(anytree)
Requires: python3dist(click)
Requires: python3dist(commonmark)
Requires: python3dist(alembic)
Requires: python3dist(blinker)
Requires: python3dist(copr-common) >= %copr_common_version
Requires: python3dist(python-dateutil)
Requires: python3dist(email-validator)
Requires: python3dist(flask)
Requires: python3dist(flask-caching)
Requires: python3dist(flask-sqlalchemy)
Requires: python3dist(flask-session)
Requires: python3dist(flask-whooshee)
Requires: python3dist(flask-wtf)
Requires: python3dist(flask-restx)
Requires: python3-gobject
Requires: python3dist(html2text)
Requires: python3dist(html5-parser)
Requires: python3dist(humanize)
Requires: python3dist(lxml)
Requires: python3dist(markdown)
Requires: python3dist(markupsafe)
Requires: python3dist(mod-wsgi)
Requires: python3dist(munch)
Requires: python3dist(netaddr)
Requires: python3dist(psycopg2)
Requires: python3dist(pygments)
Requires: python3dist(pylibravatar)
Requires: python3dist(redis)
Requires: python3dist(requests)
Requires: python3dist(templated-dictionary)
Requires: python3dist(wtforms) >= 2.2.1
Requires: python3dist(pyzmq)
Requires: python3dist(python-ldap)
Requires: python3dist(backoff) >= 1.9.0
Requires: python3dist(pygal)
Requires: python3dist(xstatic-bootstrap-scss)
Requires: python3dist(xstatic-datatables)
Requires: js-jquery-ui
Requires: python3dist(xstatic-patternfly)
Requires: modulemd-tools >= 0.6
Requires: python3dist(authlib)

Provides: bundled(bootstrap-combobox) = 1.1.6
Provides: bundled(bootstrap-select) = 1.5.4
Provides: bundled(bootstrap-treeview) = 1.0.1
Provides: bundled(c3) = 0.4.10
Provides: bundled(d3) = 3.5.0
Provides: bundled(datatables-colreorder) = 1.1.3
Provides: bundled(datatables-colvis) = 1.1.2
Provides: bundled(font-awesome) = 1.0.1
Provides: bundled(google-code-prettify) = 4.3.0

%description
COPR is lightweight build system. It allows you to create new project in WebUI,
and submit new builds and COPR will create yum repository from latests builds.

This package contains frontend.

%if %{with doc}
%package doc
Summary:    Code documentation for COPR
Obsoletes:  copr-doc < 1.38

%description doc
COPR is lightweight build system. It allows you to create new project in WebUI,
and submit new builds and COPR will create yum repository from latests builds.

This package include documentation for COPR code. Mostly useful for developers
only.
%endif

%package fedora
Summary: Template files for %{name}
Requires: %{name} = %{version}
%flavor_provides

%description fedora
Template files for %{name} (basically colors, logo, etc.).  This package is
designed to be replaced - build your replacement package against %{name}-devel
to produce compatible {name}-flavor package, then use man dnf.conf(5) 'priority'
option to prioritize your package against the default package we provide.

%package devel
Summary: Development files to build against %{name}

%description devel
Files which allow a build against %{name}, currently it's useful to build
custom %{name}-flavor package.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
%if %{with doc}
COPR_CONFIG=../../documentation/copr-documentation.conf \
  make -C documentation %{?_smp_mflags} python
%endif

%install
install -d %{buildroot}%{_sysconfdir}/copr
install -d %{buildroot}%{_datadir}/copr/coprs_frontend
install -d %{buildroot}%{_sharedstatedir}/copr/data/openid_store
install -d %{buildroot}%{_sharedstatedir}/copr/data/openid_store/associations
install -d %{buildroot}%{_sharedstatedir}/copr/data/openid_store/nonces
install -d %{buildroot}%{_sharedstatedir}/copr/data/openid_store/temp
install -d %{buildroot}%{_sharedstatedir}/copr/data/whooshee
install -d %{buildroot}%{_sharedstatedir}/copr/data/whooshee/copr_user_whoosheer
install -d %{buildroot}%{_sharedstatedir}/copr/data/srpm_storage
install -d %{buildroot}%{_sysconfdir}/cron.hourly
install -d %{buildroot}%{_sysconfdir}/cron.daily
install -d %{buildroot}/%{_bindir}
install -d %{buildroot}%{_unitdir}
install -d %{buildroot}%{_libexecdir}

install -p -m 755 conf/cron.hourly/copr-frontend* %{buildroot}%{_sysconfdir}/cron.hourly
install -p -m 755 conf/cron.daily/copr-frontend* %{buildroot}%{_sysconfdir}/cron.daily
install -p -m 755 coprs_frontend/run/copr_dump_db.sh %{buildroot}%{_libexecdir}

cp -a coprs_frontend/* %{buildroot}%{_datadir}/copr/coprs_frontend
rm -rf %{buildroot}%{_datadir}/copr/coprs_frontend/tests
sed -i "s/__RPM_BUILD_VERSION/%{version}-%{release}/" %{buildroot}%{_datadir}/copr/coprs_frontend/coprs/templates/layout.html

mv %{buildroot}%{_datadir}/copr/coprs_frontend/coprs.conf.example ./
mv %{buildroot}%{_datadir}/copr/coprs_frontend/config/* %{buildroot}%{_sysconfdir}/copr
rm %{buildroot}%{_datadir}/copr/coprs_frontend/CONTRIBUTION_GUIDELINES
touch %{buildroot}%{_sharedstatedir}/copr/data/copr.db

install -d %{buildroot}%{_var}/log/copr-frontend
install -d %{buildroot}%{_sysconfdir}/logrotate.d
cp -a conf/logrotate %{buildroot}%{_sysconfdir}/logrotate.d/%{name}
touch %{buildroot}%{_var}/log/copr-frontend/frontend.log

ln -fs /usr/share/copr/coprs_frontend/manage.py %{buildroot}/%{_bindir}/copr-frontend

mkdir -p %buildroot/$(dirname %flavor_files_list)
cat <<EOF > %buildroot%flavor_files_list
%flavor_files
EOF

mkdir -p %buildroot%macrosdir
cat <<EOF >%buildroot%macrosdir/macros.coprfrontend
%%copr_frontend_flavor_pkg \\
%flavor_provides \\
Requires: copr-frontend
%%copr_frontend_flavor_filelist   %flavor_files_list
%%copr_frontend_flavor_generator  %flavor_generator
%%copr_frontend_staticdir         %staticdir
%%copr_frontend_templatedir       %templatedir
%%copr_frontend_chroot_logodir    %%copr_frontend_staticdir/chroot_logodir
EOF

%py_byte_compile %{__python3} %{buildroot}%{_datadir}/copr/coprs_frontend/coprs
%py_byte_compile %{__python3} %{buildroot}%{_datadir}/copr/coprs_frontend/alembic

install -m0644 -D conf/copr-frontend.sysusers.conf %{buildroot}%{_sysusersdir}/copr-frontend.conf

%check
%if %{with check}
./run_tests.sh -vv --no-cov
%endif

%post
/bin/systemctl condrestart httpd.service || :
%systemd_post fm-consumer@copr_messaging.service

%preun
%systemd_preun fm-consumer@copr_messaging.service

%postun
/bin/systemctl condrestart httpd.service || :
%systemd_postun_with_restart fm-consumer@copr_messaging.service

%files
%license LICENSE
%doc coprs.conf.example
%dir %{_datadir}/copr
%dir %{_sysconfdir}/copr
%dir %{_sharedstatedir}/copr
%{_datadir}/copr/coprs_frontend
%{_bindir}/copr-frontend

%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}

%defattr(-, copr-fe, copr-fe, -)
%dir %{_sharedstatedir}/copr/data
%dir %{_sharedstatedir}/copr/data/openid_store
%dir %{_sharedstatedir}/copr/data/whooshee
%dir %{_sharedstatedir}/copr/data/whooshee/copr_user_whoosheer
%dir %{_sharedstatedir}/copr/data/srpm_storage

%ghost %{_sharedstatedir}/copr/data/copr.db

%defattr(644, copr-fe, copr-fe, 755)
%dir %{_var}/log/copr-frontend
%ghost %{_var}/log/copr-frontend/*.log

%defattr(600, copr-fe, copr-fe, 700)
%config(noreplace)  %{_sysconfdir}/copr/copr.conf
%config(noreplace)  %{_sysconfdir}/copr/copr_devel.conf
%config(noreplace)  %{_sysconfdir}/copr/copr_unit_test.conf
%config(noreplace)  %{_sysconfdir}/copr/chroots.conf

%defattr(-, root, root, -)
%config %{_sysconfdir}/cron.hourly/copr-frontend
%config %{_sysconfdir}/cron.daily/copr-frontend
%config(noreplace) %{_sysconfdir}/cron.hourly/copr-frontend-optional
%config(noreplace) %{_sysconfdir}/cron.daily/copr-frontend-optional
%{_libexecdir}/copr_dump_db.sh
%exclude_files flavor
%exclude_files devel
%{_sysusersdir}/copr-frontend.conf

%files fedora
%license LICENSE
%flavor_files

%files devel
%license LICENSE
%flavor_files_list
%devel_files
%macrosdir/*

%if %{with doc}
%files doc
%license LICENSE
%doc documentation/python-doc
%endif

%changelog
%autochangelog
