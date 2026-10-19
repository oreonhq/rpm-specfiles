%global source0_hash 336f84c3505aa0fee161d9ed97361ee2d4919e0558551bed85e66199052f6be7
%global forgeurl https://github.com/osbuild/koji-image-builder
Version:        8
%forgemeta
Name:           koji-image-builder
Release:        4%{?dist}
License:        Apache-2.0
URL:            %{forgeurl}
Source0:        %{forgeurl}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
Summary:        Koji integration plugins for image-builder
# oreon:deps
BuildRequires:  python3-devel
BuildRequires:  python3dist(koji)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-mock)
# /oreon:deps
%description
Koji integration plugins for image-builder.

%package        hub
Summary:        Koji hub plugin for image-builder integration
Requires:       %{name} = %{version}-%{release}
Requires:       koji-hub koji-hub-plugins
Requires:       python3-jsonschema
%description    hub
Koji hub plugin for image-builder integration.

%package        builder
Summary:        Koji builder plugin for image-builder integration
Requires:       %{name} = %{version}-%{release}
Requires:       koji-builder koji-builder-plugins
%description    builder
Koji builder plugin for image-builder integration.

%package        cli
Summary:        Koji cli plugin for image-cli integration
Requires:       %{name} = %{version}-%{release}
Requires:       koji python3-koji-cli-plugins
%description    cli
Koji cli plugin for image-cli integration.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgesetup

%build

%check

%pytest test/unit
%install
install -d %{buildroot}/%{_prefix}/lib/koji-hub-plugins
install -p -m 0755 plugin/hub/image_builder.py %{buildroot}/%{_prefix}/lib/koji-hub-plugins/
%py_byte_compile %{python3} %{buildroot}/%{_prefix}/lib/koji-hub-plugins/image_builder.py
install -d %{buildroot}/%{_prefix}/lib/koji-builder-plugins
install -p -m 0755 plugin/builder/image_builder.py %{buildroot}/%{_prefix}/lib/koji-builder-plugins/
%py_byte_compile %{python3} %{buildroot}/%{_prefix}/lib/koji-builder-plugins/image_builder.py
install -d %{buildroot}/%{python3_sitelib}/koji_cli_plugins
install -p -m 0644 plugin/cli/image_builder.py %{buildroot}%{python3_sitelib}/koji_cli_plugins/image_builder.py
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n koji-image-builder-hub -f %{oreon_filedir}/koji-image-builder-hub.list
%files -n koji-image-builder-builder -f %{oreon_filedir}/koji-image-builder-builder.list
%files -n koji-image-builder-cli -f %{oreon_filedir}/koji-image-builder-cli.list

%changelog

%autochangelog
