%global source0_hash 4b534d2890814939504235f1efa671127bf4342ce8a345d6b14e8082be163211

%global forgeurl https://github.com/cvmfs/collectd-cvmfs

Name:           python-collectd_cvmfs
Version:        1.4.0
%global tag     %{version}
%forgemeta
Release:        %autorelease
Summary:        Collectd plugin to monitor CvmFS Clients

License:        Apache-2.0
URL:            %{forgeurl}
Source0:        %{forgesource}
BuildArch:      noarch
 
BuildRequires:  python3-devel
# For import in checks
BuildRequires:  collectd-python

%global _description %{expand:
Collectd module for CvmFS clients. Reports time to mount as well as
other parameters vailable from the extended attributes of a CvmFS file
system.}

%description %_description

%package -n     python3-collectd_cvmfs
Summary:        %{summary}
Requires:       collectd-python

%description -n python3-collectd_cvmfs %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgesetup

%generate_buildrequires
%pyproject_buildrequires  -t

%build
%pyproject_wheel

%install
%pyproject_install

%pyproject_save_files collectd_cvmfs

%check
%tox

%files -n python3-collectd_cvmfs -f %{pyproject_files}
%license LICENSE
%{_datadir}/collectd/collectd_cvmfs.db

%changelog
%autochangelog
