%global source0_hash 59d66ef5e3c166431c39cb8b7c1d02af419051352f27912f6a43981b3def16af
%global gem_name polyglot
Name: rubygem-%{gem_name}
Version: 0.3.5
Release:        20%{?dist}
Summary:        Augment 'require' to load non-Ruby file types
License: MIT
URL: http://github.com/cjheath/polyglot
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildArch: noarch
# oreon:deps
BuildRequires:  ruby
BuildRequires:  ruby(release)
BuildRequires:  rubygems-devel
# /oreon:deps
%description
The Polyglot library allows a Ruby module to register a loader
for the file type associated with a filename extension, and it
augments 'require' to find and load matching files.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch
%description doc
Documentation for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -c -T
%gem_install -n %{SOURCE0}

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%files -f %{oreon_filedir}/main.list
%files -n rubygem-polyglot-doc -f %{oreon_filedir}/rubygem-polyglot-doc.list

%changelog

%autochangelog
