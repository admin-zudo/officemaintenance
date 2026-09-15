document.addEventListener('DOMContentLoaded', () => {
  const blogGrid = document.getElementById('blog-grid');

  if (!blogGrid) return;

  const existingCards = blogGrid.querySelectorAll('.card--blog');

  let postsData = window.blogPosts || [];

  function renderPosts(posts) {
    blogGrid.innerHTML = '';

    posts.forEach(post => {
      const article = document.createElement('article');
      article.className = 'card card--blog revealed';
      article.setAttribute('data-category', post.categoryId);

      article.innerHTML = `
        <div class="card-image" style="background-color: ${post.imageBg}; display: flex; align-items: center; justify-content: center;">
          ${post.imageHtml}
        </div>
        <div class="card-body">
          <span class="card-category">${post.category}</span>
          <h3><a href="${post.file}">${post.title}</a></h3>
          <p class="card-excerpt">${post.excerpt}</p>
          <div class="card-footer"><span>${post.author}</span><time datetime="${post.isoDate}">${post.date}</time></div>
        </div>
      `;

      blogGrid.appendChild(article);
    });
  }

  if (existingCards.length === 0 && postsData.length > 0) {
    renderPosts(postsData);
  }

  const filterTabs = document.querySelectorAll('.filter-tab');

  if (filterTabs.length > 0) {
    filterTabs.forEach(tab => {
      tab.addEventListener('click', () => {
        filterTabs.forEach(t => { t.classList.remove('active'); t.setAttribute('aria-selected', 'false'); });
        tab.classList.add('active');
        tab.setAttribute('aria-selected', 'true');

        const filter = tab.getAttribute('data-filter');

        const articles = document.querySelectorAll('.card--blog');
        articles.forEach(article => {
          if (filter === 'all' || article.getAttribute('data-category').includes(filter)) {
            article.style.display = '';
          } else {
            article.style.display = 'none';
          }
        });
      });
    });
  }
});
