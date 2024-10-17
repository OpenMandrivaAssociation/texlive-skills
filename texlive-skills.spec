Name:		texlive-skills
Version:	56734
Release:	2
Summary:	Create proficiency tests
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/skills
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/skills.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/skills.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package attempts to make it easy for even a LaTeX novice
to prepare proficiency tests, especially in combination with
the exam document class. Thus, almost all command names are
very similar. After defining skills in the preamble or in an
external file, they are declared using labels, and can
optionally be set as global skills. A skills table is generated
to summarize the evaluated competencies and to allow for
writing down the resulting proficiency level. A user's guide
attempts to explain all of the possibilities in a readable way,
with many examples.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/skills
%doc %{_texmfdistdir}/doc/latex/skills

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
