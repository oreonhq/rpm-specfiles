%global source0_hash dc08db0b568a3c72114a0004b6348628071e5ef077884c1a93138ba19de753d3
%bcond check 0
Name:           duplicity
Version:        3.2.1
Release:        1%{?dist}
Summary:        Encrypted bandwidth-efficient backup using rsync algorithm
License:        GPL-2.0-or-later AND MIT AND GPL-3.0-or-later
URL:            https://duplicity.gitlab.io/
Source0:        https://gitlab.com/duplicity/duplicity/-/archive/rel.%{version}/duplicity-rel.%{version}.tar.bz2
Patch0:         e6671cdf4ed8b21b4a8bd1973bd458f62792cd29.patch
Requires:       ca-certificates
Requires:       gnupg >= 1.0.6
Requires:       python3dist(pexpect)
Requires:  python3dist(fasteners)
Requires:       rsync
Recommends:     ncftp >= 3.1.9
Recommends:     openssh-clients
Recommends:     python3dist(boto3)
Recommends:     python3dist(dropbox)
Recommends:     python3dist(paramiko)
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(build) >= 1.1
BuildRequires:  python3dist(pip) >= 24.0
BuildRequires:  python3dist(setuptools) >= 78.1.0
BuildRequires:  python3dist(setuptools-gettext) >= 0.1.18
BuildRequires:  python3dist(wheel) >= 0.42.0
Requires:       python3-duplicity = %{version}-%{release}
# /oreon:deps
%description
Duplicity incrementally backs up files and directory by encrypting
tar-format volumes with GnuPG and uploading them to a remote (or
local) file server. In theory many protocols for connecting to a
file server could be supported; so far ssh/scp, local file access,
rsync, ftp, HSI, WebDAV and Amazon S3 have been written.

Because duplicity uses librsync, the incremental archives are space
efficient and only record the parts of files that have changed since
the last backup. Currently duplicity supports deleted files, full
unix permissions, directories, symbolic links, fifos, device files,
but not hard links.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-rel.%{version}

# Unset all the python module pins
sed -i "s/==.*$//g" requirements.txt
sed -i "s/<.*$//g" requirements.txt
sed -i "s/>=.[^\s][^,][^\"]*//g" pyproject.toml
sed -i /pipx/d pyproject.toml

# Strip requirements on optional modules not in Fedora
for i in atom boxsdk gdata-python3 gettext jottalib mediafire megatools pyrax pydrive2; do
  sed -i /"$i"/d requirements.txt
done

%build

%pyproject_wheel
%install
%pyproject_install
mkdir -p %{buildroot}/%{_sysconfdir}/%{name}
ln -sf %{_sysconfdir}/pki/tls/cert.pem \
       %{buildroot}/%{_sysconfdir}/%{name}/cacert.pem
%find_lang %{name}
rm -rf %{buildroot}%{_docdir}/duplicity-%{version}/AUTHORS.md
rm -rf %{buildroot}%{_docdir}/duplicity-%{version}/CHANGELOG.md
rm -rf %{buildroot}%{_docdir}/duplicity-%{version}/COPYING
rm -rf %{buildroot}%{_docdir}/duplicity-%{version}/README.md
rm -rf %{buildroot}%{_docdir}/duplicity-%{version}/README-LOG.md
rm -rf %{buildroot}%{_docdir}/duplicity-%{version}/README-SNAP.md
rm -rf %{buildroot}%{_docdir}/duplicity-%{version}/README-TESTING.md
rm -rf %{buildroot}%{_docdir}/duplicity-%{version}/README-REPO.md
%if %{with check}
%ifnarch ppc64le
%oreon_autofiles main

%check

%pytest -k 'not test_pylint and not test_black and not test_GzipWriteFile and not test_gpg_asym and not test_gpg_signing and not test_out_of_order_volume and not test_last_file_missing_at_end'
%endif
%endif
%files

%changelog

%autochangelog
