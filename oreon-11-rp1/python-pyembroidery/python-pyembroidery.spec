%global source0_hash 6a94658646a72fdc6966f42d0d84968f2f72438af3aa17ef2ee246a73e53e18a

%global         srcname         pyembroidery
%global         forgeurl        https://github.com/EmbroidePy/pyembroidery
Version:        1.5.1
%global         tag             %{version}
%forgemeta

Name:           python-%{srcname}
Release:        7%{?dist}
Summary:        Library for reading and writing a variety of embroidery formats

License:        MIT
URL:            %{forgeurl}
# Use source from GitHub to get license files
Source:         %{forgesource}

BuildRequires:  python3-devel

BuildArch: noarch

%global _description %{expand:
pyembroidery was coded from the ground up with all projects in mind. It
includes a lot of higher level and middle level pattern composition
abilities, and should accounts for any knowable error. If you know an error
it does not account for, raise an issue. It should be highly robust with
a simple api so as to be reasonable for any python embroidery project.

It should be complex enough to go very easily from points to stitches, fine
grained enough to let you control everything, and good enough that you
shouldn't want to.}

%description %_description

%package -n python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgeautosetup

%generate_buildrequires
%pyproject_buildrequires

%build
# Fix incorrect line endings
sed -i 's/\r$//' README.md
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{srcname}

%check
%python3 -m unittest discover test

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md
%exclude %{python3_sitelib}/test
 
%changelog
%autochangelog
