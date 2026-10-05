%global source0_hash 4a23a3c33202961cafe6c6d7ad2b157dfcd16fcc0e239908f76812ea71e81a70

%{lua:
if macros.orbs_chain_plan == nil and macros._without_bootstrap == nil then
  local spec
  local cmd = io.open("/proc/self/cmdline", "rb")
  if cmd then
    local data = cmd:read("*a") or ""
    cmd:close()
    local cur = ""
    local function take(arg)
      if string.sub(arg, -5) == ".spec" then spec = arg end
    end
    for i = 1, #data do
      local c = string.sub(data, i, i)
      if string.byte(c) == 0 then
        take(cur)
        cur = ""
      else
        cur = cur .. c
      end
    end
    take(cur)
  end
  local function trim(s)
    local a, b = 1, #s
    while a <= b do
      local c = string.sub(s, a, a)
      if c ~= " " and string.byte(c) ~= 9 then break end
      a = a + 1
    end
    while b >= a do
      local c = string.sub(s, b, b)
      if c ~= " " and string.byte(c) ~= 9 then break end
      b = b - 1
    end
    return string.sub(s, a, b)
  end
  local function miss(dep)
    local p = io.popen("dnf -q install --assumeno '" .. dep .. "' 2>&1")
    if not p then return true end
    local out = p:read("*a") or ""
    p:close()
    if string.find(out, "nothing provides", 1, true) then return true end
    if string.find(out, "No match", 1, true) then return true end
    if string.find(out, "Failed to resolve", 1, true) then return true end
    if string.find(out, "Nothing to do", 1, true) then return false end
    if string.find(out, "Operation aborted", 1, true) then return false end
    if string.find(out, "already installed", 1, true) then return false end
    return true
  end
  if spec then
    local f = io.open(spec, "r")
    if f then
      local depth, in_else, armed = 0, false, false
      for line in f:lines() do
        local s = trim(line)
        if not armed then
          if string.sub(s, 1, 3) == "%%if" and string.find(s, "{with bootstrap}", 1, true) then
            armed = true
            depth = 1
          end
        elseif string.sub(s, 1, 3) == "%%if" then
          depth = depth + 1
        elseif string.sub(s, 1, 6) == "%%endif" then
          depth = depth - 1
          if depth == 0 then break end
        elseif depth == 1 and string.sub(s, 1, 5) == "%%else" then
          in_else = true
        elseif in_else and depth == 1 and string.lower(string.sub(s, 1, 14)) == "buildrequires:" then
          local dep = trim(string.sub(s, 15))
          if dep ~= "" and string.sub(dep, 1, 1) ~= "%%" and miss(dep) then
            rpm.define("_with_bootstrap 1")
            break
          end
        end
      end
      f:close()
    end
  end
end
}
%bcond_with bootstrap

Name:           plexus-archiver
Version:        4.14.0
Release:        %autorelease
Summary:        Plexus Archiver Component
License:        Apache-2.0
URL:            https://codehaus-plexus.github.io/plexus-archiver
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

Source0:        https://github.com/codehaus-plexus/plexus-archiver/archive/refs/tags/plexus-archiver-%{version}.tar.gz#/plexus-archiver-%{version}.tar.gz

Patch:          0001-Remove-support-for-snappy-and-zstd.patch

%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(com.google.code.findbugs:jsr305)
BuildRequires:  mvn(com.google.inject:guice)
BuildRequires:  mvn(commons-io:commons-io)
BuildRequires:  mvn(javax.inject:javax.inject)
BuildRequires:  mvn(org.apache.commons:commons-compress)
BuildRequires:  mvn(org.assertj:assertj-core)
BuildRequires:  mvn(org.codehaus.plexus:plexus-io)
BuildRequires:  mvn(org.codehaus.plexus:plexus-utils)
BuildRequires:  mvn(org.codehaus.plexus:plexus:pom:)
BuildRequires:  mvn(org.eclipse.sisu:org.eclipse.sisu.inject)
BuildRequires:  mvn(org.eclipse.sisu:sisu-maven-plugin)
BuildRequires:  mvn(org.junit.jupiter:junit-jupiter-api)
BuildRequires:  mvn(org.junit.jupiter:junit-jupiter-params)
BuildRequires:  mvn(org.slf4j:slf4j-api)
BuildRequires:  mvn(org.slf4j:slf4j-simple)
BuildRequires:  mvn(org.tukaani:xz)
%endif
# TODO Remove in Fedora 46
Obsoletes:      %{name}-javadoc < 4.14.0-6

%description
The Plexus project seeks to create end-to-end developer tools for
writing applications. At the core is the container, which can be
embedded or for a full scale application server. There are many
reusable components for hibernate, form processing, jndi, i18n,
velocity, etc. Plexus also includes an application server which
is like a J2EE application server, without all the baggage.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n plexus-archiver-plexus-archiver-%{version}

%mvn_file :%{name} plexus/archiver

rm -r src/main/java/org/codehaus/plexus/archiver/snappy
rm -r src/test/java/org/codehaus/plexus/archiver/snappy
rm src/main/java/org/codehaus/plexus/archiver/tar/SnappyTarFile.java
rm src/main/java/org/codehaus/plexus/archiver/tar/PlexusIoTarSnappyFileResourceCollection.java
rm src/main/java/org/codehaus/plexus/archiver/tar/TarSnappyArchiver.java
rm src/main/java/org/codehaus/plexus/archiver/tar/TarSnappyUnArchiver.java
rm src/test/java/org/codehaus/plexus/archiver/tar/TarSnappyUnArchiverTest.java

%pom_remove_dep com.github.luben:zstd-jni
rm -r src/main/java/org/codehaus/plexus/archiver/zstd
rm -r src/test/java/org/codehaus/plexus/archiver/zstd
rm src/main/java/org/codehaus/plexus/archiver/tar/ZstdTarFile.java
rm src/main/java/org/codehaus/plexus/archiver/tar/PlexusIoTarZstdFileResourceCollection.java
rm src/main/java/org/codehaus/plexus/archiver/tar/PlexusIoTZstdFileResourceCollection.java
rm src/main/java/org/codehaus/plexus/archiver/tar/TarZstdArchiver.java
rm src/main/java/org/codehaus/plexus/archiver/tar/TarZstdUnArchiver.java
rm src/main/java/org/codehaus/plexus/archiver/tar/TZstdArchiver.java
rm src/main/java/org/codehaus/plexus/archiver/tar/TZstdUnArchiver.java
rm src/test/java/org/codehaus/plexus/archiver/tar/TarZstdUnArchiverTest.java

# Fails due to previously removed compressors
rm src/test/java/org/codehaus/plexus/archiver/manager/ArchiverManagerTest.java

%build
%mvn_build -j

%install
%mvn_install

%files -f .mfiles
%license LICENSE

%changelog
%autochangelog
