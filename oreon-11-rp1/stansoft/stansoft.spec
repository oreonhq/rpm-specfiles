%global source1_hash e7028077ef59a655db9e835a320e547f681ff5ad9259317997add2fb3739bd6f
%global source0_hash 03c3a90e80cbc3298c7819d6e524ed585b9fc508e376b69f6e54df287b0d1fee
Name:           stansoft
Version:        11.0
Release:        1%{?dist}
Summary:        Standard Accounting Software
License:        AGPL-3.0-or-later
URL:            https://www.stansoft.org
Source0:        https://download.stansoft.org/files/%{name}-%{version}.tar.bz2
Source1:        https://download.stansoft.org/files/%{name}.rpmlintrc
ExclusiveArch:  x86_64 aarch64
Requires:       aubit4gl
Requires:       libpq
Requires:       postgresql-server
Provides:  user(%{name})
Provides:  group(%{name})
# oreon:deps
BuildRequires:  aubit4gl-devel
BuildRequires:  gcc
BuildRequires:  libpq-devel
BuildRequires:  postgresql-server
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%description
Stansoft is a comprehensive double-entry financial accounting system.
It includes payroll for both the U.S. and UK. It is HMRC-recognised
for UK PAYE RTI payroll and MTD VAT returns.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%if "%{getenv:AUBITDIR}" == ""
export AUBITDIR=%{_libdir}/aubit4gl
%endif
%configure
%make_build createdb
%make_build -j1
%make_build stopdb
%install
rm -rf %{buildroot}%{_libdir}/%{name}
mkdir -p %{buildroot}%{_libdir}/%{name}
install -d %{buildroot}%{_mandir}/man1
install -p -m 0644 doc/%{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1
%make_install
cp -d %{buildroot}%{_libdir}/%{name}/lib/lib%{name}.so.* %{buildroot}%{_libdir}
rm -rf %{buildroot}%{_libdir}/%{name}/lib
mkdir -p %{buildroot}%{_bindir}
ln -sf ../..%{_libdir}/%{name}/%{name} %{buildroot}%{_bindir}/%{name}
sed -i 's:/opt:%{_libdir}:g' %{buildroot}%{_libdir}/%{name}/etc/%{name}.service
mkdir -p %{buildroot}%{_unitdir}
mv %{buildroot}%{_libdir}/%{name}/etc/%{name}.service %{buildroot}%{_unitdir}
mkdir -p %{buildroot}%{_sharedstatedir}/%{name}
sed -i 's:$SSDIR/data:%{_sharedstatedir}/%{name}/data:g' %{buildroot}%{_libdir}/%{name}/etc/postgres.sh 
sed -i 's/\(chmod 775 "\$ssdir"\)/#\1/;
        s/\(chown -R stansoft:stansoft "\$ssdir"\)/#\1/' \
        %{buildroot}%{_libdir}/%{name}/installss
rm -f %{buildroot}%{_libdir}/%{name}/README
rm -f %{buildroot}%{_libdir}/%{name}/changelog
rm -f %{buildroot}%{_libdir}/%{name}/COPYING
rm -rf %{buildroot}%{_libdir}/%{name}/doc
%oreon_autofiles main

%pre

getent group %{name} >/dev/null || groupadd -f %{name} >/dev/null 2>&1 || :
getent passwd %{name} >/dev/null || useradd -g %{name} -m \
       -s /bin/bash %{name} >/dev/null 2>&1 || exit 0
%post

%systemd_post %{name}.service
semanage fcontext -a -t postgresql_db_t '%{_sharedstatedir}/%{name}(/.*)?'
restorecon %{_sharedstatedir}/%{name}
%preun

%systemd_preun %{name}.service
%postun

%systemd_postun_with_restart %{name}.service
semanage fcontext -d -t postgresql_db_t '%{_sharedstatedir}/%{name}(/.*)?'
%check

make check
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
