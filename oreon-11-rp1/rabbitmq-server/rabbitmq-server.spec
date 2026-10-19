%global source2_hash bf3d770e522b9436d9c6bee1b1206cba6800fc64d754b1293471038eb9529138
%global source1_hash 8cbc4a91790bb76dee79d355f894c7f56e29fefc4f6146c5addde55e66c195e9
%global source0_hash ea702e5fb89ac0c8822fac820cf60bb354c8af4149337dad863f9f08072ee612
%global erlang_minver 26.2
%global _rabbit_libdir %{_exec_prefix}/lib/rabbitmq
%global debug_package %{nil}
Name: rabbitmq-server
Version: 4.3.6
Release:        1%{?dist}
Summary:        The RabbitMQ server
License: MPL-2.0
Source0:        https://github.com/rabbitmq/rabbitmq-server/releases/download/v%{version}/%{name}_%{version}.orig.tar.xz
Source1: https://github.com/rabbitmq/rabbitmq-server/releases/download/v%{version}/%{name}_%{version}.orig.tar.xz.asc
Source2: https://github.com/rabbitmq/signing-keys/releases/download/2.0/rabbitmq-release-signing-key.asc
Source3: rabbitmq-server.logrotate
Source5: rabbitmq-server.tmpfiles
Source6: rabbitmq-server-cuttlefish
Patch: rabbitmq-server-0001-Use-default-EPMD-socket.patch
Patch: rabbitmq-server-0002-Use-proto_dist-from-command-line.patch
Patch: rabbitmq-server-0003-force-python3.patch
Patch: rabbitmq-server-0004-Partially-revert-Use-template-in-rabbitmq-script-wra.patch
URL: https://www.rabbitmq.com/
Requires: erlang-eldap%{?_isa} >= %{erlang_minver}
Requires: erlang-erts%{?_isa} >= %{erlang_minver}
Requires: erlang-kernel%{?_isa} >= %{erlang_minver}
Requires: erlang-mnesia%{?_isa} >= %{erlang_minver}
Requires: erlang-os_mon%{?_isa} >= %{erlang_minver}
Requires: erlang-public_key%{?_isa} >= %{erlang_minver}
Requires: erlang-sasl%{?_isa} >= %{erlang_minver}
Requires: erlang-ssl%{?_isa} >= %{erlang_minver}
Requires: erlang-stdlib%{?_isa} >= %{erlang_minver}
Requires: erlang-syntax_tools%{?_isa} >= %{erlang_minver}
Requires: erlang-tools%{?_isa} >= %{erlang_minver}
Requires: erlang-xmerl%{?_isa} >= %{erlang_minver}
Requires: logrotate
Requires: util-linux
Requires(pre): systemd
Requires(post): systemd
Requires(preun): systemd
# oreon:deps
BuildRequires:  elixir
BuildRequires:  erlang
BuildRequires:  gnupg2
BuildRequires:  hostname
BuildRequires:  libxslt
BuildRequires:  make
BuildRequires:  python3
BuildRequires:  rsync
BuildRequires:  systemd
BuildRequires:  xmlto
BuildRequires:  zip
# /oreon:deps
%description
RabbitMQ is an implementation of AMQP, the emerging standard for high
performance enterprise messaging. The RabbitMQ server is a robust and
scalable implementation of an AMQP broker.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1

# Create a sysusers.d config file
cat >rabbitmq-server.sysusers.conf <<EOF
u rabbitmq - 'RabbitMQ messaging server' %{_localstatedir}/lib/rabbitmq -
EOF

%build

make PROJECT_VERSION=%{version} ESCRIPT_ZIP="zip -9 -X" V=1 # Doesn't support %%{?_smp_mflags}
%install
make install \
	PROJECT_VERSION=%{version} \
	ESCRIPT_ZIP="zip -9 -X" \
	DESTDIR=%{buildroot} \
	PREFIX=%{_prefix} \
	RMQ_ROOTDIR=%{_rabbit_libdir}
make install-man \
	PROJECT_VERSION=%{version} \
	ESCRIPT_ZIP="zip -9 -X" \
	DESTDIR=%{buildroot} \
	PREFIX=%{_prefix} \
	RMQ_ROOTDIR=%{_rabbit_libdir}
mkdir -p %{buildroot}%{_localstatedir}/lib/rabbitmq/mnesia
mkdir -p %{buildroot}%{_localstatedir}/log/rabbitmq
install -p -D -m 0644 ./deps/rabbit/docs/rabbitmq-server.service.example %{buildroot}%{_unitdir}/%{name}.service
install -p -D -m 0755 ./scripts/rabbitmq-script-wrapper %{buildroot}%{_sbindir}/rabbitmqctl
install -p -D -m 0755 ./scripts/rabbitmq-script-wrapper %{buildroot}%{_sbindir}/rabbitmq-server
install -p -D -m 0755 ./scripts/rabbitmq-script-wrapper %{buildroot}%{_sbindir}/rabbitmq-plugins
install -p -D -m 0755 ./scripts/rabbitmq-script-wrapper %{buildroot}%{_sbindir}/rabbitmq-diagnostics
mkdir -p %{buildroot}%{_rabbit_libdir}/bin
for app in $(basename -a %{buildroot}%{_rabbit_libdir}/lib/rabbitmq_server-%{version}/sbin/*); do
       ln -s ../lib/rabbitmq_server-%{version}/sbin/${app} %{buildroot}%{_rabbit_libdir}/bin/${app}
done
ln -s ./lib/rabbitmq_server-%{version}/plugins %{buildroot}%{_rabbit_libdir}/plugins
install -p -D -m 0755 %{S:3} %{buildroot}%{_rabbit_libdir}/bin/cuttlefish
install -p -D -m 0755 scripts/rabbitmq-server.ocf %{buildroot}%{_exec_prefix}/lib/ocf/resource.d/rabbitmq/rabbitmq-server
install -p -D -m 0644 %{S:3} %{buildroot}%{_sysconfdir}/logrotate.d/rabbitmq-server
install -p -D -m 0644 ./deps/rabbit/docs/rabbitmq.conf.example %{buildroot}%{_sysconfdir}/rabbitmq/rabbitmq.conf
install -d %{buildroot}%{_localstatedir}/run/rabbitmq
install -p -D -m 0644 %{SOURCE5} %{buildroot}%{_prefix}/lib/tmpfiles.d/%{name}.conf
install -m0644 -D rabbitmq-server.sysusers.conf %{buildroot}%{_sysusersdir}/rabbitmq-server.conf
%oreon_autofiles main

%check

%post

%systemd_post %{name}.service
%preun

%systemd_preun %{name}.service
rm -rf %{_localstatedir}/lib/rabbitmq/plugins
rm -f %{_rabbit_libdir}/lib/rabbitmq_server-%{version}/ebin/rabbit.{rel,script,boot}
%postun

%systemd_postun_with_restart %{name}.service
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
