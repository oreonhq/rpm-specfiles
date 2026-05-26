# oreon source sha256 begin
# URL sources: global sourceN_sha256 = 64-char hex from sha256sum. Omit a sourceN_sha256 line to skip verify for that source.
%global source0_sha256 0f1fb60c0df8acec48561ba561d023b55498bd04e7b3763d4ca14adaf3d62405
%global oreon_verify_sources \
%{?source0_sha256:%(test -z "%{source0_sha256}" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_sha256}" || { echo "oreon: Source0 sha256 mismatch" >&2; exit 1; }; })}
%(true)
# oreon source sha256 end

Name:           python-cheetah
Version:        3.4.0
Release:        %autorelease
Summary:        Template engine and code generator

# Most source code is MIT, except:
# BSD-3-Clause-HP:
#   Cheetah/c/_namemapper.h
# LGPL-2.1-or-later:
#   Cheetah/Utils/statprof.py
# LicenseRef-Fedora-Public-Domain:
#   Cheetah/Tests/xmlrunner.py
License:        MIT AND BSD-3-Clause-HP AND LGPL-2.1-or-later AND LicenseRef-Fedora-Public-Domain
URL:            https://cheetahtemplate.org/
Source:         https://github.com/CheetahTemplate3/cheetah3/archive/%{version}/cheetah3-%{version}.tar.gz
BuildRequires:  gcc
BuildRequires:  python3-devel

%global _description %{expand:
Cheetah3 is a free and open source template engine and code generation tool.
It can be used standalone or combined with other tools and frameworks.  Web
development is its principle use, but Cheetah is very flexible and is also
being used to generate C++ game code, Java, sql, form emails and even Python
code.}

%description %{_description}


%package -n python3-cheetah
Summary:        %{summary}


%description -n python3-cheetah %{_description}


%prep
%oreon_verify_sources
%autosetup -p1 -n cheetah3-%{version}

# remove unnecessary shebang lines to silence rpmlint
find Cheetah -type f -name '*.py' -print0 | xargs -0 sed -i -e '1 {/^#!/d}'


%generate_buildrequires
%pyproject_buildrequires -t


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files Cheetah


%check
# changing this in %%prep would cause an rpmlint error (rpm-buildroot-usage),
# so do it here instead
sed -e 's|{envsitepackagesdir}|%{buildroot}%{python3_sitearch}|' -i tox.ini
%tox


%files -n python3-cheetah -f %{pyproject_files}
%doc ANNOUNCE.rst README.rst LATEST-CHANGES.rst BUGS
%{_bindir}/cheetah*


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.4.0-1
- Prepare for Oreon 11 (RP1)
