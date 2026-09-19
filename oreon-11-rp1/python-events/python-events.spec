%global source0_hash 51fed10bad025e4bb81714b6114546b7f42773eda82df10e769d76a7859e9c3a

%global         forgeurl https://github.com/pyeve/events

Name:           python-events
Version:        0.5
%forgemeta
Release:        %autorelease
Summary:        Bringing the elegance of C# EventHandler to Python

License:        BSD-3-Clause
URL:            %{forgeurl}
Source0:        %{forgesource}

BuildArch:      noarch
 
BuildRequires:  python3-devel
BuildRequires:  python3-pytest

%global _description %{expand:
Bringing the elegance of C EventHandler to Python The C language provides a
handy way to declare, subscribe to and fire events. Technically, an event is a
"slot" where callback functions (event handlers) can be attached to a process
referred to as subscribing to an event. Here is a handy package that
encapsulates the core to event subscription and event firing and feels like a
"natural"}

%description    %_description

%package -n     python3-events
Summary:        %{summary}

%description -n python3-events %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgesetup

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%pyproject_save_files -l events

%check
%pytest events/tests/tests.py

%files -n python3-events -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
