%global source0_hash 9e15717db526f71b95f236621a56946b99a9d7353ae03c987ccca13bbb2e3b7f

Name:          buildstream-plugins
Summary:       A collection of plugins for the BuildStream project
License:       Apache-2.0
URL:           https://buildstream.build/

BuildArch:     noarch
ExcludeArch:   %{ix86}

Version:       2.8.0
Release:       %autorelease
Source0:       https://github.com/apache/buildstream-plugins/archive/%{version}/buildstream-plugins-%{version}.tar.gz

BuildRequires: python3-devel >= 3.9

Requires:      buildstream

Requires:      git
Requires:      lzip
Requires:      patch

%description
A collection of plugins for the BuildStream project

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{version} -p1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l buildstream_plugins

%files -n %{name} -f %{pyproject_files}
%doc NEWS README.rst

%changelog
%autochangelog
