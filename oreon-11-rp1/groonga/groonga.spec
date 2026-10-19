%global source0_hash e10370308607bc7b499f0ab880c4f97dd2ad89f85edcf1d2b534e301ae3fb7b3
Name:           groonga
Version:        16.1.0
Release:        1%{?dist}
Summary:        An Embeddable Fulltext Search Engine
License:        LGPL-2.1-only
URL:            https://github.com/groonga/groonga
Source0:        https://github.com/%{name}/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz
Patch:          0001-lib-grn_arrow.hpp.patch
%ifnarch %{ix86}
%endif
Requires:       %{name}-libs%{?isa} = %{version}-%{release}
Requires:       %{name}-plugin-suggest%{?isa} = %{version}-%{release}
Provides:       bundled(onigmo)
# oreon:deps
BuildRequires:  cmake
BuildRequires:  croaring-devel
BuildRequires:  gcc-c++
BuildRequires:  h3-devel
BuildRequires:  libarrow-compute-devel
BuildRequires:  libarrow-devel
BuildRequires:  libedit-devel
BuildRequires:  libevent-devel
BuildRequires:  libstemmer-devel
BuildRequires:  libzstd-devel
BuildRequires:  lz4-devel
BuildRequires:  mecab-devel
BuildRequires:  msgpack-devel
BuildRequires:  ninja-build
BuildRequires:  openssl-devel
BuildRequires:  ruby
BuildRequires:  simdjson-devel
BuildRequires:  systemd-rpm-macros
BuildRequires:  xsimd-devel
BuildRequires:  xxhash-devel
BuildRequires:  zeromq-devel
BuildRequires:  zlib-devel
# /oreon:deps
%description
Groonga is an embeddable full-text search engine library.  It can
integrate with DBMS and scripting languages to enhance their search
functionality.  It also provides a standalone data store server based
on relational data model.

%package        libs
Summary:        Runtime libraries for Groonga
License:        LGPL-2.1-only AND (MIT OR GPL-2.0-only)
%description    libs
This package contains the libraries for Groonga.

%package        devel
Summary:        Development files for Groonga
Requires:       %{name}-libs%{?isa} = %{version}-%{release}
%description    devel
This package contains libraries and header files for Groonga.

%package        server-common
Summary:        Common files for the Groonga server and the Groonga HTTP server
License:        LGPL-2.1-only
Requires:       %{name}%{?isa} = %{version}-%{release}
%description    server-common
This package provides common settings for server use.

%package        server-gqtp
Summary:        Groonga GQTP server
License:        LGPL-2.1-only
Requires:       %{name}-server-common%{?isa} = %{version}-%{release}
Requires(post): systemd
Requires(preun):systemd
%description    server-gqtp
This package contains the Groonga GQTP server.

%package        server-http
Summary:        Groonga HTTP server
License:        LGPL-2.1-only AND BSD-3-Clause
Requires:       %{name}-server-common%{?isa} = %{version}-%{release}
Requires(post): systemd
Requires(preun):systemd
%description    server-http
This package contains the Groonga HTTP server.

%package        plugin-tokenizer-mecab
Summary:        MeCab tokenizer for Groonga
Requires:       %{name}-libs%{?isa} = %{version}-%{release}
%description    plugin-tokenizer-mecab
This package contains MeCab tokenizer for Groonga.

%package        plugin-tokenizer-h3
Summary:        H3 tokenizer for Groonga
Requires:       %{name}-libs%{?isa} = %{version}-%{release}
%description    plugin-tokenizer-h3
This package contains h3 tokenizer for Groonga.

%package        plugin-suggest
Summary:        Suggest plugin for Groonga
Requires:       %{name}-libs%{?isa} = %{version}-%{release}
%description    plugin-suggest
This package contains suggest plugin for Groonga.

%package        plugin-token-filters
Summary:        Token filters plugin for Groonga
Requires:       %{name}-libs%{?isa} = %{version}-%{release}
%description    plugin-token-filters
Token filters plugins for Groonga, which provides stop word and stemming
features.

%package        munin-plugins
Summary:        Munin plugins for Groonga
Requires:       %{name}-libs%{?isa} = %{version}-%{release}
Requires:       munin-node
Requires(post): munin-node
%description    munin-plugins
This package contains munin plugins for Groonga.

%package        doc
Summary:        Documentation for Groonga
License:        LGPL-2.1-only AND BSD-3-Clause
%description doc
This package contains documentation for Groonga.

%package        examples
Summary:        Examples for Groonga
License:        LGPL-2.1-only
Requires:       %{name}%{?isa} = %{version}-%{release}
%description examples
This package contains the examples for Groonga.

%package        tools
Summary:        Tools for Groonga
License:        LGPL-2.1-only
Requires:       %{name}%{?isa} = %{version}-%{release}
%description tools
This package contains the tools for Groonga.

%prep

%autosetup -p1

rm vendor/*.tar.gz
rm vendor/*.rb
rm -rf vendor/{lz4,rapidjson-1.1.0}

# Create a sysusers.d config file
cat >groonga.sysusers.conf <<EOF
u groonga - 'groonga' %{_localstatedir}/lib/groonga -
EOF

%build

%cmake \
  -GNinja \
  -DGRN_FOR_RHEL=ON \
%ifarch riscv64
  -DCMAKE_SKIP_RPATH=TRUE \
%endif
%ifnarch %{ix86}
  -DGRN_WITH_APACHE_ARROW=ON \
%endif
  -DGRN_WITH_ZLIB=ON \
  -DGRN_WITH_ZSTD=ON \
  -DGRN_WITH_RAPIDJSON=ON \
  -DGRN_WITH_MECAB=ON \
  -DGRN_WITH_KYTEA=OFF \
  -DGRN_WITH_LIBSTEMMER=ON \
  -DGRN_WITH_ZEROMQ=ON \
  -DGRN_WITH_LIBEVENT=ON \
  -DGRN_WITH_MESSAGE_PACK=ON \
  -DGRN_WITH_XXHASH=ON \
  -DGRN_WITH_LZ4=ON \
  -DGRN_WITH_ROARING_BITMAPS=ON \
  -DGRN_WITH_BLOSC=no \
  -DGRN_WITH_XSIMD=ON \
  -DGRN_WITH_H3=ON \
  -DGRN_WITH_LLAMA_CPP=no \
  -DGRN_WITH_MRUBY=ON \
  -DGRN_WITH_MUNIN_PLUGINS=ON \
  -DGRN_WITH_DOC=ON \
  -DGRN_WITH_EXAMPLES=ON \
  -DGRN_WITH_TOOLS=ON \
  -DCMAKE_INSTALL_SYSCONFDIR=%{_sysconfdir}
%cmake_build
%install
%cmake_install
rm %{buildroot}%{_datadir}/groonga/{COPYING,README.md}
mkdir -p %{buildroot}%{_localstatedir}/lib/groonga/db
mkdir -p %{buildroot}%{_localstatedir}/log/groonga
mkdir -p %{buildroot}%{_libdir}/groonga/plugins/normalizers
mkdir -p %{buildroot}%{_sysconfdir}/munin/plugin-conf.d/
cat <<EOC > %{buildroot}%{_sysconfdir}/munin/plugin-conf.d/groonga
[groonga_*]
  user groonga
  group groonga
  env.PATH %{_bindir}
  env.database_path %{_localstatedir}/lib/groonga/db/db
  env.host 127.0.0.1
  env.http_host 127.0.0.1
  env.http_port 10041
  env.http_database_path %{_localstatedir}/lib/groonga/db/db
  env.http_pid_path %{_rundir}/groonga/groonga-http.pid
  env.http_query_log_path %{_localstatedir}/log/groonga/query-http.log
  env.gqtp_host 127.0.0.1
  env.gqtp_port 10043
  env.gqtp_database_path %{_localstatedir}/lib/groonga/db/db
  env.gqtp_pid_path %{_rundir}/groonga/groonga-gqtp.pid
  env.gqtp_query_log_path %{_localstatedir}/log/groonga/query-gqtp.log
EOC
install -m0644 -D groonga.sysusers.conf %{buildroot}%{_sysusersdir}/groonga.conf
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%post munin-plugins

%{_sbindir}/munin-node-configure --shell --remove-also | grep -e 'groonga_' | sh
%systemd_postun munin-node
%pre server-common

if [ $1 = 1 ] ; then
  mkdir -p %{_localstatedir}/log/groonga
  mkdir -p %{_localstatedir}/lib/groonga/db
  groonga -n %{_localstatedir}/lib/groonga/db/db shutdown > /dev/null
  chown -R groonga:groonga %{_localstatedir}/log/groonga
  chown -R groonga:groonga %{_localstatedir}/lib/groonga
  mkdir -p %{_localstatedir}/run/groonga
  chown -R groonga:groonga %{_localstatedir}/run/groonga
fi
exit 0
%post server-gqtp

%systemd_post groonga-server-gqtp.service
%preun server-gqtp

%systemd_preun groonga-server-gqtp.service
%postun server-gqtp

%systemd_postun groonga-server-gqtp.service
%post server-http

%systemd_post groonga-server-http.service
%preun server-http

%systemd_preun groonga-server-http.service
%postun server-http

%systemd_postun groonga-server-http.service
%postun munin-plugins

if [ $1 -eq 0 ]; then
    [ -f %{_localstatedir}/lock/subsys/munin-node ] && \
        systemctl restart munin-node >/dev/null 2>&1
    :
fi
%files -f %{oreon_filedir}/main.list
%files -n groonga-libs -f %{oreon_filedir}/groonga-libs.list
%files -n groonga-devel -f %{oreon_filedir}/groonga-devel.list
%files -n groonga-server-common -f %{oreon_filedir}/groonga-server-common.list
%files -n groonga-server-gqtp -f %{oreon_filedir}/groonga-server-gqtp.list
%files -n groonga-server-http -f %{oreon_filedir}/groonga-server-http.list
%files -n groonga-plugin-tokenizer-mecab -f %{oreon_filedir}/groonga-plugin-tokenizer-mecab.list
%files -n groonga-plugin-tokenizer-h3 -f %{oreon_filedir}/groonga-plugin-tokenizer-h3.list
%files -n groonga-plugin-suggest -f %{oreon_filedir}/groonga-plugin-suggest.list
%files -n groonga-plugin-token-filters -f %{oreon_filedir}/groonga-plugin-token-filters.list
%files -n groonga-munin-plugins -f %{oreon_filedir}/groonga-munin-plugins.list
%files -n groonga-doc -f %{oreon_filedir}/groonga-doc.list
%files -n groonga-examples -f %{oreon_filedir}/groonga-examples.list
%files -n groonga-tools -f %{oreon_filedir}/groonga-tools.list

%changelog

%autochangelog
