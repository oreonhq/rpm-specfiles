%global source0_hash none

Name:           python-beanprice
Version:        2.1.0
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Price quotes fetcher for Beancount

# No license information obtained, it's up to the packager to fill it in
License:        ...
URL:            https://github.com/beancount/beanprice
Source:         %{pypi_source beanprice}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'beanprice' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-beanprice
Summary:        %{summary}

%description -n python3-beanprice %_description


%prep
%autosetup -p1 -n beanprice-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-beanprice -f %{pyproject_files}
%{_bindir}/bean-price

%changelog
%autochangelog
