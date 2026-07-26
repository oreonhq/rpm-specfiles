%global source0_hash a07313b2d2b4240ccdc88f82577807cf85063d53f7ddd9be00db43469e6f7fa7

%global pypi_name accept-types
%global pypi_version 0.4.1
%global commit cb2531768689478737e4a8454def6a60575424e3
%global shortcommit %(c=%{commit}; echo ${c:0:12})
%global owner tim_heap

Name:           python-%{pypi_name}
Version:        %{pypi_version}
Release:        18%{?dist}
Summary:        Use the correct accept type for an HTTP request
License:        MIT
URL:            https://bitbucket.org/%{owner}/%{name}
# The pypi source has the test suite stripped out :/
Source0:        %{URL}/get/%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel

%global desc \
accept-types helps your application respond to a HTTP request in a way \
that a client prefers.  The Accept header of an HTTP request informs the \
server which MIME types the client is expecting back from this request, \
with weighting to indicate the most prefered. If your server can respond \
in multiple formats (e.g.: JSON, XML, HTML), the client can easily tell \
your server which is the prefered format without resorting to hacks like \
'&amp;format=json' on the end of query strings.

%description
%{desc}

%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name}
%{desc}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{owner}-%{name}-%{shortcommit}
%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel

%check
%tox

%install
%pyproject_install
%pyproject_save_files accept_types

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
