%global source0_hash eb836e155fff00dba2feddece25f2ef89cf49bb5b75812f3ebeb5cd6e8c8449b

%global pypi_name pypubsub
%global src_name Pypubsub

Name:           python-pypubsub
Version:        4.0.7
Release:        1%{?dist}
Summary:        Python Publish-Subscribe Package

License:        BSD-2-Clause
URL:            https://github.com/schollii/pypubsub
Source0:        https://github.com/schollii/pypubsub/archive/v%{version}.tar.gz#/%{src_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-pytest

%description
PyPubSub provides a publish - subscribe API that facilitates the development of
event-based / message-based applications. PyPubSub supports sending and
receiving messages between objects of an application. It is centered on the
notion of a topic; senders publish messages of a given topic, and listeners
subscribe to messages of a given topic. The package also supports a variety of
advanced features that facilitate debugging and maintaining pypubsub topics and
messages in larger applications.

%package -n     python3-pypubsub
Summary:        %{summary}

%description -n python3-pypubsub
PyPubSub provides a publish - subscribe API that facilitates the development of
event-based / message-based applications. PyPubSub supports sending and
receiving messages between objects of an application. It is centered on the
notion of a topic; senders publish messages of a given topic, and listeners
subscribe to messages of a given topic. The package also supports a variety of
advanced features that facilitate debugging and maintaining pypubsub topics and
messages in larger applications.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files pubsub

%check
%pyproject_check_import

pushd tests/suite
PYTHONPATH=%{buildroot}%{python3_sitelib} PYTHONDONTWRITEBYTECODE=1 py.test-%{python3_version}
popd

%files -n python3-pypubsub -f %{pyproject_files}
%doc README.rst src/pubsub/RELEASE_NOTES.txt
%license src/pubsub/LICENSE_BSD_Simple.txt

%changelog
%autochangelog
