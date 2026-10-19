%global source0_hash f75ee691956dc48f3ff2730c018808fc8c44caf6ab755cf752c84cec10ee7282
%global	gem_name	tk
Name:		rubygem-%{gem_name}
Version:	0.6.0
Release:        1%{?dist}
Summary:        Tk interface module using tcltklib
License:	BSD-2-Clause OR Ruby
URL:		https://github.com/ruby/tk
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Patch0:	rubygem-tk-pr82-fix-tk9-regex.patch
Patch1:	rubygem-tk-pr84-fix-frozen_error-on-demo.patch
Obsoletes:		ruby-tcltk < 2.4.0
# oreon:deps
BuildRequires:  gcc
BuildRequires:  pkgconfig(tk)
BuildRequires:  ruby(release)
BuildRequires:  ruby-devel
BuildRequires:  rubygems-devel
# /oreon:deps
%description
Tk interface module using tcltklib.

%package	doc
Summary:	Documentation for %{name}
License:	(BSD-2-Clause OR Ruby) AND TCL AND MIT-CMU
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch
%description doc
Documentation for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version}
mv ../%{gem_name}-%{version}.gemspec .

%patch -P0 -p1
%patch -P1 -p1

%build

grep -rlZ /usr/local/bin . | \
	xargs -0 sed -i -e 's|/usr/local/bin|%{_bindir}|g'
grep -rlZ /usr/bin/env . | \
	xargs -0 sed -i -e 's|/usr/bin/env ruby|%{_bindir}/ruby|'
find . -name \*.rb -print0 | xargs -0 grep -lZ '^#![ \t]*%{_bindir}' | \
	xargs -0 sed -i -e '\@^#![ \t]*%{_bindir}@d'
find . -name \*.rb -print0 | xargs -0 chmod 0644
find sample -type f -print0 | xargs -0 grep -lZ '^#![ \t]*%{_bindir}' | \
	xargs -0 chmod 0755
gem build %{gem_name}-%{version}.gemspec
%gem_install
%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
	%{buildroot}%{gem_dir}/
mkdir -p %{buildroot}%{gem_extdir_mri}
cp -a .%{gem_extdir_mri}/* \
	%{buildroot}%{gem_extdir_mri}/
rm -f %{buildroot}%{gem_cache}
pushd %{buildroot}%{gem_instdir}
rm -rf \
	.github \
	.gitignore \
	.travis.yml \
	Gemfile \
	README.macosx-aqua \
	README.tcltklib \
	Rakefile \
	old-README.tcltklib.ja \
	%{gem_name}.gemspec \
	bin/ \
	ext/ \
	%{nil}
popd
pushd %{buildroot}%{gem_extdir_mri}
rm -f \
	mkmf.log \
	gem_make.out \
	%{nil}
popd
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%files -f %{oreon_filedir}/main.list
%files -n rubygem-tk-doc -f %{oreon_filedir}/rubygem-tk-doc.list

%changelog

%autochangelog
