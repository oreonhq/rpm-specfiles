%global source0_hash 20a543b39b4a86caef11decd402c1f511da4bc3858eda5cdd0fdb38e33526a4a
Name:           python-compreffor
Version:        0.6.0
Release:        1%{?dist}
Summary:        CFF table subroutinizer for FontTools
License:        Apache-2.0
URL:            https://github.com/googlefonts/compreffor
Source0:        https://github.com/googlefonts/compreffor/archive/v%{version}/compreffor-%{version}.tar.gz
Source1:        compreffor.1
ExcludeArch:    %{ix86}
%global common_description %{expand:
A CFF (Compact Font Format) table subroutinizer for FontTools.}
# oreon:deps
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  tomcli
# /oreon:deps
%description %{common_description}

%package -n python3-compreffor
Summary:        CFF table subroutinizer for FontTools
%description -n python3-compreffor %{common_description}

%prep

%autosetup -p1
# Drop the setuptools_git_ls_files dependency
#
# This dependency makes sense upstream, but we do not need it (and it is
# not packaged) in Fedora.
tomcli set pyproject.toml lists delitem 'build-system.requires' \
    'setuptools_git_ls_files\b.*'

# Remove shebangs from non-script sources. The find-then-modify pattern
# preserves mtimes on sources that did not need to be modified.
find 'src' -type f -name '*.py' \
    -exec gawk '/^#!/ { print FILENAME }; { nextfile }' '{}' '+' |
  xargs -r sed -r -i '1{/^#!/d}'

# Remove Cython-generated sources; we must ensure they are regenerated.
find src/cython -type f -name '*.c*' -print -delete

# Do not use requirements.txt for tox dependencies, as it contains (only) an
# overly-strict pinned fonttools version.
sed -r -i '/^[[:blank:]]*-rrequirements.txt[[:blank:]]*/d' 'tox.ini'

%build -p

export SETUPTOOLS_SCM_PRETEND_VERSION='%{version}'
%install
%pyproject_install
install -t '%{buildroot}%{_mandir}/man1' -p -m 0644 -D '%{SOURCE1}'
%oreon_autofiles python3-compreffor usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%tox
%files -f %{oreon_filedir}/main.list
%files -n python3-compreffor -f %{oreon_filedir}/python3-compreffor.list

%changelog

%autochangelog
