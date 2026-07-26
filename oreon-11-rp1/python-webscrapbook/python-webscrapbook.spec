%global source0_hash 061c4e0aa4fe7961fb2059edcc36385f72c9ba57d2febf35dc55bfdcad36ea99

# Initially created by pyp2rpm-3.3.2
%global pypi_name webscrapbook

#%%global gitdate 20240526
#%%global gitref 48ad89d28e811fe4fc633e5071bd874c76caddee
#%%global shortref %%(echo %%{gitref} |cut -c1-8)

%if 0%{?shortref:1}
%global buildref .%{gitdate}git%{shortref}
%endif

%if 0%{?gitref:1}
%global directoryname PyWebScrapbook-%{gitref}
%global archivename %{directoryname}.tar.gz
%global dlpath archive/%{gitref}.tar.gz
%else
%global directoryname PyWebScrapBook-%{version}
%global archivename %{directoryname}.zip
%global dlpath archive/refs/tags/%{version}.zip
%endif

Name:           python-%{pypi_name}
Version:        2.7.2
Release:        2%{?dist}
Summary:        A backend toolkit for management of WebScrapBook collection

License:        MIT
URL:            https://github.com/danny0838/PyWebScrapBook
Source0:        %{url}/%{dlpath}#/%{archivename}

# Downstream Fedora patch to comply with packaging guidelines
Patch100:       python-webscrapbook-2.7.1-test-requirements.patch

BuildArch:      noarch
BuildRequires:  python3-devel
# For mime.types
BuildRequires:  mailcap

%global _description %{expand:
PyWebScrapBook is a command line toolkit and backend server for the
WebScrapBook browser extension.

Features: Host any directory as a website; HTZ or MAFF archive file viewing;
Markdown file rendering; Directory listing; Create, view, edit, and/or delete
files via the web page or API; HTTP(S) authorization.}

%description %_description

%package -n     python3-%{pypi_name}
Summary:        %{summary}
Recommends:     python3-%{pypi_name}+adhoc_ssl
 
%description -n python3-%{pypi_name} %_description

%pyproject_extras_subpkg -n python3-%{pypi_name} adhoc_ssl

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{directoryname}

%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel

%install
%pyproject_install

%pyproject_save_files webscrapbook

%check
%tox

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md
%{_bindir}/webscrapbook
%{_bindir}/wsb
%{_bindir}/wsbview

%changelog
%autochangelog
