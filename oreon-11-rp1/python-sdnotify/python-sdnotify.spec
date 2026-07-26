%global source0_hash 73977fc746b36cc41184dd43c3fe81323e7b8b06c2bb0826c4f59a20c56bb9f1

Name:           python-sdnotify
Version:        0.3.2
Release:        %autorelease
License:        MIT
Summary:        A pure Python implementation of systemd's service notification protocol
URL:            https://github.com/bb4242/sdnotify
Source0:        %{pypi_source sdnotify}
BuildArch:      noarch

BuildRequires: python3-devel

Requires: systemd

%global _description %{expand:
This is a pure Python implementation of the systemd sd_notify protocol. This
protocol can be used to inform systemd about service start-up completion,
watchdog events, and other service status changes. Thus, this package can be
used to write system services in Python that play nicely with systemd. sdnotify
is compatible with both Python 2 and Python 3.
}

%description %_description

%package -n     python3-sdnotify
Summary:        %{summary}

%description -n python3-sdnotify %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n sdnotify-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files sdnotify

%check
# NOTE(neil) - 2023-01-25 upstream does not provide any tests yet
%pyproject_check_import

%files -n python3-sdnotify -f %{pyproject_files}
%license LICENSE.txt

%changelog
%autochangelog
