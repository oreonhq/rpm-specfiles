%global source0_hash none

Name:           python-twisted
Version:        26.4.0
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        An asynchronous networking framework written in Python

# No license information obtained, it's up to the packager to fill it in
License:        ...
URL:            https://twisted.org/
Source:         %{pypi_source twisted}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'twisted' generated automatically by pyp2spec.}

Patch0:         python-twisted-25.5.0-disable-tests.patch
Patch1:         0001-Fix-asyncio-get_event_loop-for-Python-3-14.patch
Patch2:         0002-Fix-web-client-urljoin-for-Python-3-14.patch
Patch3:         0003-Fix-tests-for-Python-3-14-2.patch

%description %_description

%package -n     python3-twisted
Summary:        %{summary}

%description -n python3-twisted %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-twisted all-non-platform,all-non-platform,conch,dev,dev-release,dev-release,gtk-platform,gtk-platform,http2,macos-platform,macos-platform,mypy,osx-platform,osx-platform,serial,test,tls,websocket,windows-platform,windows-platform


%prep
%autosetup -p1 -n twisted-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x all-non-platform,all-non-platform,conch,dev,dev-release,dev-release,gtk-platform,gtk-platform,http2,macos-platform,macos-platform,mypy,osx-platform,osx-platform,serial,test,tls,websocket,windows-platform,windows-platform


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-twisted -f %{pyproject_files}
%{_bindir}/cftp
%{_bindir}/ckeygen
%{_bindir}/conch
%{_bindir}/mailmail
%{_bindir}/pyhtmlizer
%{_bindir}/tkconch
%{_bindir}/trial
%{_bindir}/twist
%{_bindir}/twistd

%changelog
%autochangelog
