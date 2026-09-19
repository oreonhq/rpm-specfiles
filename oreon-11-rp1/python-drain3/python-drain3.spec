%global source0_hash 32915d64a2b5637f9d58cca33095bc147c9cc754e69b718a011ca30a2d8aa4c5

# the 0.9.11 is old without a release, so packaging recent snapshot
# see https://github.com/logpai/Drain3/issues/98
%global commit 76d12defdeec14da3794d451875b781669f62acf
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global project Drain3

Name:           python-drain3
Version:        0.9.11
Release:        20240424git%{shortcommit}.%autorelease
Summary:        Persistent & streaming log template miner

# drain3/simple_profiler.py is Apache-2.0
License:        MIT AND Apache-2.0
URL:            https://github.com/IBM/Drain3
Source:         https://github.com/logpai/%{project}/archive/%{commit}/%{project}-%{shortcommit}.tar.gz
#Source:         %%{pypi_source drain3}

BuildArch:      noarch
BuildRequires:  python3-devel
#tests
BuildRequires:  python3-kafka
BuildRequires:  python3-redis

# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
Drain3 is an online log template miner that can extract templates (clusters)
from a stream of log messages in a timely manner. It employs a parse tree with
fixed depth to guide the log group search process, which effectively avoids
constructing a very deep and unbalanced tree.}

%description %_description

%package -n     python3-drain3
Summary:        %{summary}
Suggests:       python3-kafka
Suggests:       python3-redis

%description -n python3-drain3 %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{project}-%{commit}
#%%autosetup -p1 -n drain3-%%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files 'drain3'

%check
%pyproject_check_import

%files -n python3-drain3 -f %{pyproject_files}
%license LICENSE.txt
%doc README.md

%changelog
%autochangelog
