%global source0_hash ad565f26ecb92588a3e43bc3d96164de84cd9902482b130d0ddbaa9664a85065

%global common_description %{expand:
wsproto is a pure-Python implementation of a WebSocket protocol stack.  It is
written from the ground up to be embeddable in whatever program you choose to
use, ensuring that you can communicate via WebSockets, as defined in RFC6455,
regardless of your programming paradigm.

wsproto does not provide a parsing layer, a network layer, or any rules about
concurrency.  Instead, it is a purely in-memory solution, defined in terms of
data actions and WebSocket frames.  RFC6455 and Compression Extensions for
WebSocket via RFC7692 are fully supported.}

%bcond_without  tests

Name:           python-wsproto
Version:        1.2.0
Release:        %autorelease
Summary:        WebSockets state-machine based protocol implementation
License:        MIT
URL:            https://github.com/python-hyper/wsproto
Source:         %{pypi_source wsproto}
BuildArch:      noarch

%description %{common_description}

%package -n python3-wsproto
Summary:        %{summary}
BuildRequires:  python3-devel
%if %{with tests}
BuildRequires:  python3-pytest
%endif

%description -n python3-wsproto %{common_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n wsproto-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l wsproto

%check
%if %{with tests}
%pytest --verbose
%else
%pyproject_check_import
%endif

%files -n python3-wsproto -f %{pyproject_files}
%doc README.rst CHANGELOG.rst

%changelog
%autochangelog
