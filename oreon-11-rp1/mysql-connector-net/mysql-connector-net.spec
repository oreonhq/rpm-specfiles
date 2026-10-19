%global source0_hash 9aabb27240ea2c0499315cce85628df70cd3db8b90f9bc5ac26e1248ff26d8ca
%global debug_package %{nil}
Name:           mysql-connector-net
Version:        9.2.0
Release:        1%{?dist}
Summary:        Mono ADO.NET driver for MySQL
License:        GPL-2.0-only AND LicenseRef-Callaway-BSD
URL:            http://dev.mysql.com/downloads/connector/net/
Source0:        http://cdn.mysql.com/Downloads/Connector-Net/%{name}-%{version}-src.zip
Source1:        mysql-connector-net.pc
Requires:       mono-data >= 4.0
ExclusiveArch: %{mono_arches}
# oreon:deps
BuildRequires:  mono-devel
# /oreon:deps
%description
Connector/Net is a fully-managed ADO.NET driver for MySQL.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig
%description devel
Development files for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -c
#Avoid sign the assembly due problem with the key
sed -i '77i#if DEBUG' Source/MySql.Data/Properties/AssemblyInfo.cs
sed -i '80i#endif' Source/MySql.Data/Properties/AssemblyInfo.cs
sed -i '81i[assembly: AssemblyKeyName("ConnectorNet")]' Source/MySql.Data/Properties/AssemblyInfo.cs

%build

xbuild /property:Configuration=Release /property:VisualStudioVersion=11.0 Source/MySql.Data/MySql.Data.csproj
%install
%{__mkdir_p} %{buildroot}/%{_libdir}/pkgconfig
%{__mkdir_p} %{buildroot}/%{_monogacdir}/
%{__mkdir_p} %{buildroot}/%{_monodir}/mysql-connector-net/
install -p -m0644 %SOURCE1 %{buildroot}%{_libdir}/pkgconfig/
%{__install} -m0755 Source/MySql.Data/bin/v4.5/Release/MySql.Data.dll %{buildroot}%{_monodir}/mysql-connector-net/
gacutil -i %{buildroot}%{_monodir}/mysql-connector-net/MySql.Data.dll -f -package mysql-connector-net -root %{buildroot}/%{_prefix}/lib
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n mysql-connector-net-devel -f %{oreon_filedir}/mysql-connector-net-devel.list

%changelog

%autochangelog
