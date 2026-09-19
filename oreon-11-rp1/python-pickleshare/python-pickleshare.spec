%global source0_hash 87683d47965c1da65cdacaf31c8441d12b8044cdec9aca500cd78fc2c683afca

Name:           python-pickleshare
Version:        0.7.5
Release:        24%{?dist}
Summary:        Tiny 'shelve'-like database with concurrency support

License:        MIT
URL:            https://github.com/ipython/pickleshare
Source:         %{pypi_source pickleshare}

BuildArch:      noarch
 
BuildRequires:  python3-devel

%global _description %{expand:
PickleShare - a small ‘shelve’ like data store with concurrency support.

Like shelve, a PickleShareDB object acts like a normal dictionary. 
Unlike shelve, many processes can access the database simultaneously. 
Changing a value in database is immediately visible to other processes 
accessing the same database.

Concurrency is possible because the values are stored in separate files. 
Hence the “database” is a directory where all files are governed 
by PickleShare.}

%description %_description

%package -n     python3-pickleshare
Summary:        %{summary}

%description -n python3-pickleshare %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n pickleshare-%{version}

# fix interpreter
sed -i 's/\/usr\/bin\/env python/\/usr\/bin\/python/' pickleshare.py

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
# Must do the subpackages' install first because the scripts in /usr/bin are
# overwritten with every setup.py install.
%pyproject_install
%pyproject_save_files -l pickleshare

%check
%pyproject_check_import

%files -n python3-pickleshare -f %{pyproject_files}

%changelog
%autochangelog
