# oreon source sha256 begin
# URL sources: global sourceN_sha256 = 64-char hex from sha256sum. Omit a sourceN_sha256 line to skip verify for that source.
%global source0_sha256 f5c2b7733ca731d15bab3defb177e2a705ab6cea02230969c7a1559e5dd4cdb9
%global oreon_verify_sources \
%{?source0_sha256:%(test -z "%{source0_sha256}" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_sha256}" || { echo "oreon: Source0 sha256 mismatch" >&2; exit 1; }; })}
%(true)
# oreon source sha256 end

Name:           pf-bb-config
Version:        24.07
Release:        4%{?dist}
Summary:        PF BBDEV (baseband device) Configuration Application

License:        Apache-2.0
URL:            https://github.com/intel/pf-bb-config
Source0:        https://github.com/intel/pf-bb-config/archive/v24.07/pf-bb-config-24.07.tar.gz

# Currently big endian is not supported due to a bug
ExcludeArch:    s390x

BuildRequires:  gcc
BuildRequires:  make


%description
The PF BBDEV (baseband device) Configuration Application "pf_bb_config"
provides a means to configure the baseband device at the host-level.
The program accesses the configuration space and sets the various parameters
through memory-mapped IO read/writes.


%prep
%oreon_verify_sources
%autosetup -p1
sed -i "s/#VERSION_STRING#/%{version}/g" config_app.c


%build
%make_build CFLAGS="${RPM_OPT_FLAGS}" LDFLAGS="${RPM_LD_FLAGS}"


%install
for dir in acc100 agx100 fpga_5gnr fpga_lte vrb1 vrb2; do
	install -d -m 755 %{buildroot}%{_datadir}/pf-bb-config/$dir/
	cp -a $dir/*.cfg %{buildroot}%{_datadir}/pf-bb-config/$dir/
done
install -d -m 755 %{buildroot}%{_bindir}
install -p -D -m 755 pf_bb_config %{buildroot}%{_bindir}/pf_bb_config


%files
%license LICENSE
%doc README.md
%{_bindir}/pf_bb_config
%{_datadir}/pf-bb-config/


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 24.07-4
- Prepare for Oreon 11 (RP1)
